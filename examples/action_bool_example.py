#!/usr/bin/env python3
"""action_boolの実行例。

このスクリプトは、action_boolとSimpliseClient.action.executeを使用して
実際にAPIを呼び出し、結果を確認するサンプルコードです。
.envファイルからAPIキーを読み込みます。

実行方法:
    1. .env.example を .env にコピー
    2. .env ファイル内の SIMPLISE_API_KEY に実際のAPIキーを設定
    3. python examples/action_bool_example.py を実行
"""

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from simplise_api_client.actions.data.bool import action_bool
from simplise_api_client.base import SimpliseClient


def main() -> None:
    """action_boolの実行例を実演する。"""
    # [AI GENERATED] Setup logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # [AI GENERATED] Load .env file
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(env_path)

    # [AI GENERATED] 環境変数からAPIキーを取得
    api_key = os.getenv("SIMPLISE_API_KEY")
    if not api_key:
        logger.error("エラー: .envファイルで SIMPLISE_API_KEY が設定されていません")
        logger.error("設定方法: .envファイルに SIMPLISE_API_KEY='your_actual_api_key' を追加してください")
        sys.exit(1)

    # [AI GENERATED] SimpliseClientを作成
    client = SimpliseClient(api_key=api_key)

    logger.info("action_boolの実行例")
    logger.info("=" * 50)

    # [AI GENERATED] テストケース: (入力値, 期待結果)
    test_cases = [
        # 数値から論理値
        (0, "false"),  # 0 → false
        (1, "true"),  # 0以外の数値 → true
        (42, "true"),  # 0以外の数値 → true
        (-1, "true"),  # 0以外の数値 → true
        (0.0, "false"),  # 0.0 → false
        (1.5, "true"),  # 0以外の数値 → true
        # 文字列から論理値
        ("", "false"),  # 空文字列 → false
        ("false", "false"),  # "false" (大文字小文字無視) → false
        ("FALSE", "false"),  # "FALSE" (大文字小文字無視) → false
        ("0", "false"),  # 数値文字列で0を表すもの → false
        ("0.0", "false"),  # 数値文字列で0.0を表すもの → false
        ("-0", "false"),  # 数値文字列で-0を表すもの → false
        ("00", "false"),  # 数値文字列で00を表すもの → false
        (" ", "true"),  # スペースを含むその他の文字列 → true
        ("hello", "true"),  # その他の文字列 → true
        ("1", "true"),  # 0以外の数値文字列 → true
        ("true", "true"),  # "true"文字列 → true
        # 配列から論理値
        ([], "false"),  # 空配列 → false
        ([1], "true"),  # 要素を持つ配列 → true
        # オブジェクトから論理値
        ({}, "false"),  # 空オブジェクト → false
        ({"key": "value"}, "true"),  # プロパティを持つオブジェクト → true
        # 特殊値
        (None, "false"),  # null → false
        # 既存の論理値
        (True, "true"),  # 既存の論理値 → そのまま返却
        (False, "false"),  # 既存の論理値 → そのまま返却
    ]

    for value, expected in test_cases:
        try:
            # [AI GENERATED] action_bool操作を作成
            bool_operation = action_bool(value)

            # [AI GENERATED] APIを実行
            result = client.action.execute(bool_operation)

            # [AI GENERATED] 結果を表示
            status = "✓" if result == expected else "✗"
            logger.info(f"{status} action_bool({value!r}) -> {result} (期待値: {expected})")

        except Exception:
            logger.exception(f"✗ action_bool({value!r}) -> エラー")

    logger.info("=" * 50)
    logger.info("実行完了")


if __name__ == "__main__":
    main()
