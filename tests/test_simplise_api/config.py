"""テスト設定管理モジュール"""

from loguru import logger
from pydantic import Field
from pydantic_settings import BaseSettings


class TestConfig(BaseSettings):
    """テスト設定クラス

    Simplise APIのテストに必要な設定を管理します。
    環境変数からの設定読み込みもサポートしています。
    """

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "env_prefix": "SIMPLISE_TEST_",
        "extra": "ignore",
    }

    base_url: str = Field(default="https://api.usebootstrap.org", description="APIのベースURL")

    bearer_token: str = Field(default="API_KEY", description="Bearer認証トークン")

    timeout: int = Field(default=30, description="リクエストタイムアウト（秒）")

    retry_count: int = Field(default=3, description="リトライ回数")

    log_level: str = Field(default="INFO", description="ログレベル")



# グローバル設定インスタンス
test_config = TestConfig()


logger.info(f"テスト設定を読み込みました: {test_config.base_url}")
