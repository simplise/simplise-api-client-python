"""pytest設定ファイル

テスト全体で使用される設定とフィクスチャを定義します。
"""

import asyncio
import sys
from collections.abc import Generator
from pathlib import Path

import pytest
from loguru import logger

# プロジェクトルートをPythonパスに追加
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """セッションスコープのイベントループフィクスチャ

    非同期テスト用のイベントループを提供します。
    """
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def setup_logging():
    """自動適用されるログ設定フィクスチャ

    各テスト実行時に適切なログフォーマットを設定します。
    """
    # 既存のロガーを削除
    logger.remove()

    # テスト用のログフォーマットを設定
    logger.add(
        sys.stdout,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> | <level>{message}</level>",  # noqa: E501
        level="INFO",
    )

    return logger


def pytest_configure(config) -> None:
    """pytest設定の初期化

    テスト実行前の設定を行います。
    """
    # カスタムマーカーの追加
    config.addinivalue_line("markers", "integration: 統合テストマーカー")
    config.addinivalue_line("markers", "unit: ユニットテストマーカー")
    config.addinivalue_line("markers", "slow: 実行時間が長いテストマーカー")


def pytest_collection_modifyitems(config, items) -> None:
    """テスト収集後の処理

    収集されたテストアイテムに対して追加の設定を行います。
    """
    for item in items:
        # 非同期テストにマーカーを自動追加
        if "asyncio" in item.keywords:
            item.add_marker(pytest.mark.integration)
