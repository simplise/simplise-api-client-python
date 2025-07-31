"""simplise-api-clientテスト用のテスト設定とフィクスチャ。

このモジュールには、Simplise APIクライアントライブラリをテストするための
pytestフィクスチャと設定が含まれています。テストクライアントインスタンスとサンプルデータを提供します。
"""

import pytest

from simplise_api_client.base import SimpliseClient


@pytest.fixture
def api_key() -> str:
    """テストAPIキーフィクスチャを返す。

    個別のテストで値をハードコーディングしないように、
    テストケース全体で一貫したテストAPIキーを提供します。

    Returns:
        str: テスト用のAPIキー文字列。
    """
    return "test_api_key_123"


@pytest.fixture
def base_url() -> str:
    """テストベースURLフィクスチャを返す。

    個別のテストで値をハードコーディングしないように、
    テストケース全体で一貫したテストベースURLを提供します。

    Returns:
        str: テスト用のベースURL文字列。
    """
    return "https://test.example.com"


@pytest.fixture
def client(api_key: str, base_url: str) -> SimpliseClient:
    """SimpliseClientインスタンスフィクスチャを返す。

    複数のテストケースで一貫したテストのために
    テストフィクスチャを使用してSimpliseClientインスタンスを作成します。

    Args:
        api_key (str): api_keyフィクスチャからのテストAPIキー。
        base_url (str): base_urlフィクスチャからのテストベースURL。

    Returns:
        SimpliseClient: テスト用に設定されたクライアントインスタンス。
    """
    return SimpliseClient(api_key=api_key, base_url=base_url)


@pytest.fixture
def sample_json_logic_rule() -> dict:
    """サンプルJsonLogicルールフィクスチャを返す。

    ルール処理と実行機能をテストするための
    サンプルJsonLogicルールを提供します。

    Returns:
        dict: 条件ロジックをテストするためのサンプルJsonLogicルール。
    """
    return {"if": [{"==": [{"var": "age"}, 25]}, "Adult", "Minor"]}


@pytest.fixture
def sample_input_data() -> dict:
    """サンプル入力データフィクスチャを返す。

    データを使用したルール実行の包括的なテストのために、
    サンプルJsonLogicルールに対応するサンプル入力データを提供します。

    Returns:
        dict: age、name、emailフィールドを含むサンプル入力データ。
    """
    return {"age": 25, "name": "John Doe", "email": "john@example.com"}
