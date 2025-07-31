"""action_boolとSimpliseClient.action.executeの実際のAPI統合テスト。

このモジュールには、実際のSimplise APIを使用した統合テストが含まれています。
.envファイルから実際のAPIキーを読み込み、本番エンドポイントでテストします。

使用方法:
1. .env.example を .env にコピー
2. .env ファイル内の SIMPLISE_API_KEY に実際のAPIキーを設定
3. このファイルを pytest で実行

例:
    cp .env.example .env
    # .env ファイルを編集してAPIキーを設定
    pytest tests/actions/data/test_bool_integration_real.py -v
"""

import os
from pathlib import Path

import pytest
from dotenv import load_dotenv

from simplise_api_client.actions.data.bool import action_bool
from simplise_api_client.base import SimpliseClient


class TestActionBoolIntegrationReal:
    """action_boolとSimpliseClient.action.executeの実際のAPI統合テスト。

    このクラスには、実際のSimplise APIを使用したテストケースが含まれています。
    テストを実行するには、実際のAPIキーが必要です。
    """

    @pytest.fixture
    def real_client(self) -> SimpliseClient:
        """実際のAPIキーを使用したSimpliseClientを返す。

        .envファイルからAPIキーを読み込み、クライアントインスタンスを作成します。

        Returns:
            SimpliseClient: 実際のAPIキーを使用したクライアントインスタンス

        Raises:
            pytest.skip: .envファイルまたはAPIキーが設定されていない場合はテストをスキップ
        """
        # [AI GENERATED] .envファイルをロード（プロジェクトルートから）
        env_path = Path(__file__).parent.parent.parent.parent / ".env"
        if env_path.exists():
            load_dotenv(env_path)
        else:
            pytest.skip(f".env file not found at {env_path}")

        api_key = os.getenv("SIMPLISE_TEST_BEARER_TOKEN")
        if not api_key:
            pytest.skip("SIMPLISE_TEST_BEARER_TOKEN not set in .env file")

        base_url = os.getenv("SIMPLISE_API_URL", "https://api.usebootstrap.org")
        return SimpliseClient(api_key=api_key, base_url=base_url)

    def test_action_bool_execute_with_test_cases_real(self, real_client: SimpliseClient) -> None:
        """action_boolのテストケースと期待結果をチェックして実際のAPIでテスト。

        定義されたテストケースに対してaction_boolの動作を検証し、
        期待される結果と一致することを確認します。

        Args:
            real_client: 実際のAPIキーを使用したSimpliseClientインスタンス
        """
        # [AI GENERATED] テストケース: (入力値, 期待結果)
        test_cases = [
            # 数値から論理値
            (0, "false"),  # 0 → false
            (1, "true"),  # 0以外の数値 → true
            (42, "true"),  # 0以外の数値 → true
            (-1, "true"),  # 0以外の数値 → true
            (0.0, "false"),  # 0.0 → false
            (1.5, "true"),  # 0以外の数値 → true
            (-3.14, "true"),  # 0以外の数値 → true
            # 文字列から論理値
            ("", "false"),  # 空文字列 → false
            ("false", "false"),  # "false" (大文字小文字無視) → false
            ("FALSE", "false"),  # "FALSE" (大文字小文字無視) → false
            ("False", "false"),  # "False" (大文字小文字無視) → false
            ("0", "false"),  # 数値文字列で0を表すもの → false
            ("0.0", "false"),  # 数値文字列で0を表すもの → false
            ("-0", "false"),  # 数値文字列で0を表すもの → false
            ("00", "false"),  # 数値文字列で0を表すもの → false
            ("0e10", "false"),  # 数値文字列で0を表すもの → false
            (" ", "true"),  # スペースを含むその他の文字列 → true
            ("hello", "true"),  # その他の文字列 → true
            ("1", "true"),  # 0以外の数値文字列 → true
            ("true", "true"),  # "true"文字列 → true
            # 配列から論理値
            # TODO: 配列とオブジェクト、nullは別のメソッドを使用する必要があるため、一時的にテストから除外
            # ([], "false"),  # 空配列 → false
            # ([1], "true"),  # 要素を持つ配列 → true
            # ([0], "true"),  # 要素を持つ配列 → true
            # ([""], "true"),  # 要素を持つ配列 → true
            # オブジェクトから論理値
            # ({}, "false"),  # 空オブジェクト → false
            # ({"key": "value"}, "true"),  # プロパティを持つオブジェクト → true
            # ({"a": 1}, "true"),  # プロパティを持つオブジェクト → true
            # 特殊値
            # (None, "false"),  # null → false
            # 既存の論理値
            (True, "true"),  # 既存の論理値 → そのまま返却
            (False, "false"),  # 既存の論理値 → そのまま返却
        ]

        # [AI GENERATED] 各テストケースを実行
        for input_value, expected_result in test_cases:
            bool_operation = action_bool(input_value)
            result = real_client.action.execute(bool_operation)
            assert result == expected_result, (
                f"action_bool({input_value!r}) -> Expected '{expected_result}', got '{result}'"
            )
