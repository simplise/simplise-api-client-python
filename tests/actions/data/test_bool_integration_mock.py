"""action_boolとSimpliseClient.action.executeのモック統合テスト。

このモジュールには、action_boolとSimpliseClient.action.executeを組み合わせた
モックAPIを使用した統合テストが含まれています。
"""

from unittest.mock import Mock, patch

from simplise_api_client.actions.data.bool import action_bool
from simplise_api_client.base import SimpliseClient

# [AI GENERATED] 定数定義
DEFAULT_TIMEOUT = 30.0


class TestActionBoolIntegrationMock:
    """action_boolとSimpliseClient.action.executeのモック統合テスト。

    このクラスには、action_boolとSimpliseClient.action.executeを組み合わせた
    モックAPIレスポンスを使用したテストケースが含まれています。
    """

    @patch("simplise_api_client.base.requests.post")
    def test_action_bool_execute_with_test_cases_mock(self, mock_post: Mock) -> None:
        """action_boolのテストケースと期待結果をチェックしてモックでテスト。

        定義されたテストケースに対してaction_boolの動作を検証し、
        期待される結果と一致することをモックAPIで確認します。
        """
        # [AI GENERATED] テストケース: (入力値, 期待結果, 期待されるJSON)
        test_cases = [
            # 数値から論理値
            (0, "false", '{"bool": ["0"]}'),  # 0 → false
            (1, "true", '{"bool": ["1"]}'),  # 0以外の数値 → true
            (42, "true", '{"bool": ["42"]}'),  # 0以外の数値 → true
            (-1, "true", '{"bool": ["-1"]}'),  # 0以外の数値 → true
            (0.0, "false", '{"bool": ["0.0"]}'),  # 0.0 → false
            (1.5, "true", '{"bool": ["1.5"]}'),  # 0以外の数値 → true
            # 文字列から論理値
            ("", "false", '{"bool": [""]}'),  # 空文字列 → false
            ("false", "false", '{"bool": ["false"]}'),  # "false" → false
            ("FALSE", "false", '{"bool": ["FALSE"]}'),  # "FALSE" → false
            ("False", "false", '{"bool": ["False"]}'),  # "False" → false
            ("0", "false", '{"bool": ["0"]}'),  # 数値文字列で0 → false
            ("0.0", "false", '{"bool": ["0.0"]}'),  # 数値文字列で0.0 → false
            ("-0", "false", '{"bool": ["-0"]}'),  # 数値文字列で-0 → false
            ("00", "false", '{"bool": ["00"]}'),  # 数値文字列で00 → false
            ("0e10", "false", '{"bool": ["0e10"]}'),  # 数値文字列で0e10 → false
            (" ", "true", '{"bool": [" "]}'),  # スペース → true
            ("hello", "true", '{"bool": ["hello"]}'),  # その他の文字列 → true
            ("1", "true", '{"bool": ["1"]}'),  # 0以外の数値文字列 → true
            ("true", "true", '{"bool": ["true"]}'),  # "true" → true
            # 配列から論理値
            ([], "false", '{"bool": [[]]}'),  # 空配列 → false
            ([1], "true", '{"bool": [["1"]]}'),  # 要素を持つ配列 → true
            # オブジェクトから論理値
            ({}, "false", '{"bool": [{}]}'),  # 空オブジェクト → false
            ({"a": 1}, "true", '{"bool": [{"a": "1"}]}'),  # プロパティを持つオブジェクト → true
            # 特殊値
            (None, "false", '{"bool": [null]}'),  # null → false
            # 既存の論理値
            (True, "true", '{"bool": ["True"]}'),  # 既存の論理値 → そのまま
            (False, "false", '{"bool": ["False"]}'),  # 既存の論理値 → そのまま
        ]

        # [AI GENERATED] テスト用クライアントを作成
        client = SimpliseClient(api_key="test_key", base_url="https://test.example.com")

        # [AI GENERATED] 各テストケースを実行
        for input_value, expected_result, expected_json in test_cases:
            # [AI GENERATED] モックをリセット
            mock_post.reset_mock()

            # [AI GENERATED] モックレスポンスを設定
            mock_response = Mock()
            mock_response.text = expected_result
            mock_response.raise_for_status.return_value = None
            mock_post.return_value = mock_response

            # [AI GENERATED] bool操作を作成
            bool_operation = action_bool(input_value)

            # [AI GENERATED] SimpliseClient.action.executeで実行
            result = client.action.execute(bool_operation)

            # [AI GENERATED] 結果が期待値と一致することを検証
            assert result == expected_result, (
                f"action_bool({input_value!r}) -> Expected '{expected_result}', got '{result}'"
            )

            # [AI GENERATED] リクエストが正しく送信されたことを検証
            mock_post.assert_called_once()
            call_args = mock_post.call_args

            # [AI GENERATED] リクエストデータが正しいことを確認
            assert call_args[1]["files"]["action"][1] == expected_json, (
                f"Expected JSON {expected_json} for input {input_value!r}, got {call_args[1]['files']['action'][1]}"
            )

    @patch("simplise_api_client.base.requests.post")
    def test_action_bool_request_format_validation(self, mock_post: Mock) -> None:
        """action_boolのリクエスト形式が正しいことを検証するテスト。

        リクエストが期待される形式（multipart/form-data）で送信され、
        正しいヘッダーとデータが含まれることを確認します。
        """
        # [AI GENERATED] モックレスポンスを設定
        mock_response = Mock()
        mock_response.text = "false"
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        # [AI GENERATED] テスト用クライアントを作成
        client = SimpliseClient(api_key="test_api_key", base_url="https://test.example.com")

        # [AI GENERATED] action_bool(0)を実行
        bool_operation = action_bool(0)
        client.action.execute(bool_operation)

        # [AI GENERATED] リクエストが一度だけ呼ばれたことを確認
        mock_post.assert_called_once()

        # [AI GENERATED] 呼び出し引数を取得
        call_args = mock_post.call_args

        # [AI GENERATED] URLが正しいことを確認
        expected_url = "https://test.example.com/action-logic"
        assert call_args[0][0] == expected_url

        # [AI GENERATED] ヘッダーにAuthorizationが含まれることを確認
        headers = call_args[1]["headers"]
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer test_api_key"

        # [AI GENERATED] multipart/form-dataとしてactionデータが送信されることを確認
        files = call_args[1]["files"]
        assert "action" in files
        action_data = files["action"]
        assert action_data[1] == '{"bool": ["0"]}'
        assert action_data[2] == "application/json"

        # [AI GENERATED] タイムアウトが設定されていることを確認
        timeout = call_args[1]["timeout"]
        assert timeout == DEFAULT_TIMEOUT
