"""テスト基底クラスとユーティリティ"""

import json
from typing import Any
from urllib.parse import urlencode

import aiohttp
from loguru import logger
from pydantic import BaseModel

from .config import test_config

# 定数定義
STATUS_SUCCESS = 200
STATUS_CREATED = 201
STATUS_NO_CONTENT = 204
STATUS_MULTIPLE_CHOICES = 300
STATUS_ERROR = 400


def check_success(status_code: int) -> bool:
    """ステータスコードが成功かどうかを判定"""
    return STATUS_SUCCESS <= status_code < STATUS_MULTIPLE_CHOICES


class APIResponse(BaseModel):
    """APIレスポンスモデル

    Simplise APIからのレスポンスを表現するモデルです。
    """

    status_code: int
    headers: dict[str, str]
    content: dict[str, Any] | list[Any] | str | bytes
    is_success: bool

    @property
    def is_error(self) -> bool:
        """エラーレスポンスかどうかを判定"""
        return not self.is_success


class SimpliseAPIClient:
    """Simplise API クライアント

    Simplise APIとの通信を行うためのクライアントクラスです。
    GET/POSTリクエストの送信、レスポンスの解析などを行います。
    """

    def __init__(self, base_url: str | None = None, bearer_token: str | None = None) -> None:
        """クライアントの初期化

        Args:
            base_url: APIのベースURL（省略時は設定ファイルの値を使用）
            bearer_token: Bearer認証トークン（省略時は設定ファイルの値を使用）
        """
        self.base_url = base_url or test_config.base_url
        self.bearer_token = bearer_token or test_config.bearer_token
        self._session: aiohttp.ClientSession | None = None

    @property
    def session(self) -> aiohttp.ClientSession:
        """aiohttpのセッションを取得

        Returns:
            aiohttp.ClientSession: セッションオブジェクト
        """
        if self._session is None:
            err_msg = "Session is not initialized. Use 'async with SimpliseAPIClient() as client:' to create a session."
            logger.error(err_msg)
            raise RuntimeError(err_msg)
        return self._session

    async def __aenter__(self) -> "SimpliseAPIClient":
        """非同期コンテキストマネージャーの開始"""
        self._session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=test_config.timeout),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.bearer_token}"},
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # noqa: ANN001
        """非同期コンテキストマネージャーの終了"""
        if self.session:
            await self.session.close()

    async def get_action(self, params: dict[str, Any]) -> APIResponse:
        """GETリクエストで/actionエンドポイントを呼び出し

        Args:
            params: クエリパラメータ

        Returns:
            APIResponse: レスポンス情報
        """
        url = f"{self.base_url}/action"
        query_string = urlencode(params)
        full_url = f"{url}?{query_string}"

        logger.info(f"GET リクエスト送信: {full_url}")

        try:
            async with self.session.get(full_url) as response:
                content = await self._parse_response_content(response)

                return APIResponse(
                    status_code=response.status,
                    headers=dict(response.headers),
                    content=content,
                    is_success=check_success(response.status),
                )
        except Exception as e:
            logger.error(f"GET リクエストでエラーが発生: {e}")
            raise

    async def post_action(self, data: dict[str, Any]) -> APIResponse:
        """POSTリクエストで/actionエンドポイントを呼び出し

        Args:
            data: リクエストボディのデータ

        Returns:
            APIResponse: レスポンス情報
        """
        url = f"{self.base_url}/action"

        logger.info(f"POST リクエスト送信: {url}")
        logger.debug(f"リクエストボディ: {json.dumps(data, ensure_ascii=False)}")

        try:
            async with self.session.post(url, json=data) as response:
                content = await self._parse_response_content(response)

                return APIResponse(
                    status_code=response.status,
                    headers=dict(response.headers),
                    content=content,
                    is_success=check_success(response.status),
                )
        except Exception as e:
            logger.error(f"POST リクエストでエラーが発生: {e}")
            raise

    async def get_logic(self, params: dict[str, Any]) -> APIResponse:
        """GETリクエストで/logicエンドポイントを呼び出し

        Args:
            params: クエリパラメータ

        Returns:
            APIResponse: レスポンス情報
        """
        url = f"{self.base_url}/logic"
        query_string = urlencode(params)
        full_url = f"{url}?{query_string}"

        logger.info(f"GET リクエスト送信（ロジック）: {full_url}")

        try:
            async with self.session.get(full_url) as response:
                content = await self._parse_response_content(response)

                return APIResponse(
                    status_code=response.status,
                    headers=dict(response.headers),
                    content=content,
                    is_success=check_success(response.status),
                )
        except Exception as e:
            logger.error(f"GET リクエスト（ロジック）でエラーが発生: {e}")
            raise

    async def _parse_response_content(self, response: aiohttp.ClientResponse) -> dict[str, Any] | str:
        """レスポンス内容を解析

        Args:
            response: aiohttp レスポンスオブジェクト

        Returns:
            解析されたレスポンス内容（JSON形式またはテキスト）
        """
        try:
            content_type = response.headers.get("Content-Type", "")
            if "application/json" in content_type:
                return await response.json()
            return await response.text()
        except Exception as e:
            logger.warning(f"レスポンス解析でエラー: {e}")
            return await response.text()


class BaseTestCase:
    """テスト基底クラス

    Simplise APIのテストケースで共通して使用される機能を提供します。
    """

    def __init__(self) -> None:
        """テストケースの初期化"""
        self.client: SimpliseAPIClient | None = None

    async def setup(self) -> None:
        """テストケースのセットアップ

        各テストケース実行前に呼び出される処理です。
        """
        logger.info("テストケースのセットアップを開始")
        self.client = SimpliseAPIClient()

    async def teardown(self) -> None:
        """テストケースのクリーンアップ

        各テストケース実行後に呼び出される処理です。
        """
        logger.info("テストケースのクリーンアップを開始")
        if self.client:
            # クライアントのクリーンアップは__aexit__で行われるため、ここでは何もしない
            pass

    def assert_response_status(self, response: APIResponse, expected_status: int) -> None:
        """レスポンスステータスのアサーション

        Args:
            response: APIレスポンス
            expected_status: 期待するステータスコード

        Raises:
            AssertionError: ステータスコードが期待値と異なる場合
        """
        assert response.status_code == expected_status, (
            f"期待したステータスコード: {expected_status}, "
            f"実際のステータスコード: {response.status_code}, "
            f"レスポンス: {response.content}"
        )

    class ResponseNotJsonError(TypeError):
        """レスポンスがJSON形式でない場合の例外"""

        def __init__(self, content: Any) -> None:  # noqa: ANN401
            msg = f"レスポンスがJSON形式ではありません: {content}"
            super().__init__(msg)

    def assert_response_contains_key(self, response: APIResponse, key: str) -> None:
        """レスポンスに指定したキーが含まれるかのアサーション

        Args:
            response: APIレスポンス
            key: 確認するキー名

        Raises:
            AssertionError: キーが含まれていない場合
            ResponseNotJsonError: レスポンスがJSON形式でない場合
        """
        if isinstance(response.content, dict):
            assert key in response.content, (
                f"レスポンスにキー '{key}' が含まれていません。レスポンス: {response.content}"
            )
        elif isinstance(response.content, list):
            assert any(key in item for item in response.content), (
                f"レスポンスのリスト内にキー '{key}' が含まれていません。レスポンス: {response.content}"
            )
        else:
            raise self.ResponseNotJsonError(response.content)
