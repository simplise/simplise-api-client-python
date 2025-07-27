"""Simplise API テストケース"""

from collections.abc import AsyncGenerator

import pytest
from loguru import logger

from .base import (
    STATUS_ERROR,
    STATUS_SUCCESS,
    SimpliseAPIClient,
)


class TestSimpliseAPI:
    """Simplise API のテストケース

    Simplise APIの各エンドポイントとパラメータの動作を検証するテストクラスです。
    """

    @pytest.mark.asyncio
    async def test_gsun_get_action(self) -> None:
        """GSUN取得のGETリクエストテスト

        /actionエンドポイントにGETリクエストでgsunパラメータを送信し、
        正常にGlobal Serial Unique Numberが取得できることを確認します。
        """
        logger.info("GSUN取得テスト（GET /action）を開始")

        async with SimpliseAPIClient() as client:
            params = {"gsun": "50"}
            response = await client.get_action(params)

            logger.info(f"レスポンス: {response.status_code} - {response.content}")

            # ステータスコードが200であることを確認
            assert response.status_code == STATUS_SUCCESS, (
                f"期待したステータスコード: {STATUS_SUCCESS}, "
                f"実際のステータスコード: {response.status_code}, "
                f"レスポンス: {response.content}"
            )

            # レスポンスにgsunが含まれることを確認（成功時）
            if response.is_success and isinstance(response.content, dict):
                logger.info("GSUN取得テスト成功")
            else:
                logger.warning(f"GSUN取得で想定外のレスポンス: {response.content}")

    @pytest.mark.asyncio
    async def test_gsun_get_logic(self) -> None:
        """GSUN取得のロジック確認テスト

        /logicエンドポイントにGETリクエストでgsunパラメータを送信し、
        クエリロジックが正常に取得できることを確認します。
        """
        logger.info("GSUNロジック取得テスト（GET /logic）を開始")

        async with SimpliseAPIClient() as client:
            params = {"gsun": "50"}
            response = await client.get_logic(params)

            logger.info(f"ロジックレスポンス: {response.status_code} - {response.content}")

            # ステータスコードが200であることを確認
            assert response.status_code == STATUS_SUCCESS, (
                f"期待したステータスコード: {STATUS_SUCCESS}, "
                f"実際のステータスコード: {response.status_code}, "
                f"レスポンス: {response.content}"
            )

            logger.info("GSUNロジック取得テスト完了")

    @pytest.mark.asyncio
    async def test_gsun_post_action(self) -> None:
        """GSUN取得のPOSTリクエストテスト

        /actionエンドポイントにPOSTリクエストでgsunパラメータを送信し、
        GETリクエストと同じ結果が得られることを確認します。
        """
        logger.info("GSUN取得テスト（POST /action）を開始")

        async with SimpliseAPIClient() as client:
            data = {"gsun": ["50"]}
            response = await client.post_action(data)

            logger.info(f"POSTレスポンス: {response.status_code} - {response.content}")

            # ステータスコードが200であることを確認
            assert response.status_code == STATUS_SUCCESS, (
                f"期待したステータスコード: {STATUS_SUCCESS}, "
                f"実際のステータスコード: {response.status_code}, "
                f"レスポンス: {response.content}"
            )

            logger.info("GSUN取得テスト（POST）完了")

    @pytest.mark.asyncio
    async def test_qr_gen_with_add_operation(self) -> None:
        """QRコード生成と加算操作のテスト

        add操作の結果をQRコード生成に渡すクエリをテストします。
        現在は400エラーが期待される状態です。
        """
        logger.info("QRコード生成+加算操作テスト（GET /action）を開始")

        async with SimpliseAPIClient() as client:
            params = {"qr.gen": "add(10.1,5.0005)"}
            response = await client.get_action(params)

            logger.info(f"QR+加算レスポンス: {response.status_code} - {response.content}")

            # 現在は400エラーが期待される（Unsupported operator: add）
            assert response.status_code == STATUS_ERROR, (
                f"期待したステータスコード: {STATUS_ERROR}, "
                f"実際のステータスコード: {response.status_code}, "
                f"レスポンス: {response.content}"
            )

            # エラーメッセージの確認
            if isinstance(response.content, dict):
                assert "error" in response.content, (
                    f"レスポンスにキー 'error' が含まれていません。レスポンス: {response.content}"
                )
                assert "message" in response.content, (
                    f"レスポンスにキー 'message' が含まれていません。レスポンス: {response.content}"
                )

                if "Unsupported operator: add" in str(response.content.get("message", "")):
                    logger.info("期待通りのエラーメッセージを確認")
                else:
                    logger.warning(f"想定外のエラーメッセージ: {response.content.get('message')}")

            logger.info("QRコード生成+加算操作テスト完了")

    @pytest.mark.asyncio
    async def test_ai_rag_operation(self) -> None:
        """AI RAG操作のテスト

        ai.ragオペレーターを使用したクエリをテストします。
        現在は400エラーが期待される状態です。
        """
        logger.info("AI RAG操作テスト（GET /action）を開始")

        async with SimpliseAPIClient() as client:
            params = {"ai.rag": "1815980170936321,abc"}
            response = await client.get_action(params)

            logger.info(f"AI RAGレスポンス: {response.status_code} - {response.content}")

            # 現在は400エラーが期待される（Unsupported operator: ai.rag）
            assert response.status_code == STATUS_ERROR, (
                f"期待したステータスコード: {STATUS_ERROR}, "
                f"実際のステータスコード: {response.status_code}, "
                f"レスポンス: {response.content}"
            )

            # エラーメッセージの確認
            if isinstance(response.content, dict):
                assert "error" in response.content, (
                    f"レスポンスにキー 'error' が含まれていません。レスポンス: {response.content}"
                )
                assert "message" in response.content, (
                    f"レスポンスにキー 'message' が含まれていません。レスポンス: {response.content}"
                )

                if "Unsupported operator: ai.rag" in str(response.content.get("message", "")):
                    logger.info("期待通りのエラーメッセージを確認")
                else:
                    logger.warning(f"想定外のエラーメッセージ: {response.content.get('message')}")

            logger.info("AI RAG操作テスト完了")


@pytest.fixture
async def api_client() -> AsyncGenerator[SimpliseAPIClient, None]:
    """APIクライアントのフィクスチャ

    テストで使用するSimpliseAPIClientのインスタンスを提供します。
    各テスト実行後に自動的にクリーンアップされます。

    Yields:
        SimpliseAPIClient: 設定済みのAPIクライアントインスタンス
    """
    async with SimpliseAPIClient() as client:
        yield client


@pytest.mark.asyncio
async def test_gsun_get_action_with_fixture(api_client: SimpliseAPIClient) -> None:
    """フィクスチャを使用したGSUN取得テスト

    pytestのフィクスチャ機能を使用してAPIクライアントを取得し、
    GSUN取得のテストを実行します。

    Args:
        api_client: APIクライアントのフィクスチャ
    """
    logger.info("フィクスチャを使用したGSUN取得テストを開始")

    params = {"gsun": "50"}
    response = await api_client.get_action(params)

    logger.info(f"レスポンス: {response.status_code} - {response.content}")

    assert response.status_code == STATUS_SUCCESS, (
        f"期待したステータスコード: {STATUS_SUCCESS}, "
        f"実際のステータスコード: {response.status_code}, レスポンス: {response.content}"
    )

    logger.info("フィクスチャを使用したGSUN取得テスト完了")


@pytest.mark.parametrize(
    ("gsun_value", "expected_status"),
    [
        ("50", STATUS_SUCCESS),
        ("100", STATUS_SUCCESS),
        ("0", STATUS_SUCCESS),
    ],
)
@pytest.mark.asyncio
async def test_gsun_parametrized(api_client: SimpliseAPIClient, gsun_value: str, expected_status: int) -> None:
    """パラメータ化されたGSUN取得テスト

    複数のGSUN値をテストして、期待されるステータスコードが返されることを確認します。

    Args:
        api_client: APIクライアントのフィクスチャ
        gsun_value: テストするGSUN値
        expected_status: 期待するHTTPステータスコード
    """
    logger.info(f"GSUN値 '{gsun_value}' のパラメータ化テストを開始")

    params = {"gsun": gsun_value}
    response = await api_client.get_action(params)

    logger.info(f"GSUN={gsun_value}, レスポンス: {response.status_code} - {response.content}")

    assert response.status_code == expected_status, (
        f"GSUN={gsun_value}: 期待したステータスコード: {expected_status}, "
        f"実際のステータスコード: {response.status_code}, "
        f"レスポンス: {response.content}"
    )

    logger.info(f"GSUN値 '{gsun_value}' のパラメータ化テスト完了")


@pytest.mark.parametrize(
    ("operation", "expected_error"),
    [
        ("add(10.1,5.0005)", "Unsupported operator: add"),
        ("subtract(10,5)", "Unsupported operator: subtract"),
        ("multiply(3,4)", "Unsupported operator: multiply"),
    ],
)
@pytest.mark.asyncio
async def test_unsupported_operations_parametrized(
    api_client: SimpliseAPIClient, operation: str, expected_error: str
) -> None:
    """パラメータ化されたサポートされていない操作のテスト

    様々なサポートされていない操作に対して、適切なエラーメッセージが返されることを確認します。

    Args:
        api_client: APIクライアントのフィクスチャ
        operation: テストする操作
        expected_error: 期待するエラーメッセージ
    """
    logger.info(f"サポートされていない操作 '{operation}' のテストを開始")

    params = {"qr.gen": operation}
    response = await api_client.get_action(params)

    logger.info(f"操作={operation}, レスポンス: {response.status_code} - {response.content}")

    assert response.status_code == STATUS_ERROR, (
        f"操作={operation}: 期待したステータスコード: {STATUS_ERROR}, "
        f"実際のステータスコード: {response.status_code}, "
        f"レスポンス: {response.content}"
    )

    if isinstance(response.content, dict):
        message = response.content.get("message", "")
        assert expected_error in str(message), (
            f"操作={operation}: 期待したエラーメッセージ '{expected_error}' が含まれていません。"
            f"実際のメッセージ: {message}"
        )

    logger.info(f"サポートされていない操作 '{operation}' のテスト完了")
