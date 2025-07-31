"""SimpliseClient基本機能のテスト。

このモジュールには、SimpliseClient基本機能の包括的なテストケースが含まれています。
クライアント初期化、アクションロジックAPI、アクション実行機能をテストします。
"""

from typing import TYPE_CHECKING
from unittest.mock import Mock, patch

import pytest

from simplise_api_client.base import Action, ActionLogicAPI, SimpliseClient

if TYPE_CHECKING:
    from simplise_api_client.type import JsonLogicRule


class TestSimpliseClient:
    """SimpliseClientのテストケース。

    様々な設定やデフォルト値でのSimpliseClient初期化を
    検証するためのテストケースが含まれています。
    """

    def test_client_initialization_with_all_parameters(self) -> None:
        """全パラメーターでのSimpliseClient初期化をテスト。

        すべてのパラメーター（api_key、base_url、timeout）が
        明示的に提供された場合のSimpliseClientの正しい初期化を検証します。
        """
        # [AI GENERATED] テストパラメーターを定義
        api_key = "test_api_key"
        base_url = "https://test.example.com"
        timeout = 60.0

        # [AI GENERATED] 全パラメーターでSimpliseClientを初期化
        client = SimpliseClient(api_key=api_key, base_url=base_url, timeout=timeout)

        # [AI GENERATED] すべてのパラメーターが正しく設定されることを検証
        assert client.api_key == api_key, f"Expected api_key '{api_key}', got '{client.api_key}'"
        assert client.base_url == base_url, f"Expected base_url '{base_url}', got '{client.base_url}'"
        assert client.timeout == timeout, f"Expected timeout {timeout}, got {client.timeout}"

        # [AI GENERATED] actionとaction_logicインスタンスが適切に初期化されることを検証
        assert isinstance(client.action, Action), f"Expected Action instance, got {type(client.action)}"
        assert isinstance(client.action_logic, ActionLogicAPI), (
            f"Expected ActionLogicAPI instance, got {type(client.action_logic)}"
        )

    def test_client_initialization_with_default_values(self) -> None:
        """デフォルト値でのSimpliseClient初期化をテスト。

        api_keyのみが提供された場合に、SimpliseClientが
        base_urlとtimeoutに正しいデフォルト値を使用することを検証します。
        """
        # [AI GENERATED] 必須パラメーターのみを定義
        api_key = "test_api_key"
        expected_default_base_url = "https://api.usebootstrap.org"
        expected_default_timeout = 30.0

        # [AI GENERATED] 最小パラメーターでSimpliseClientを初期化
        client = SimpliseClient(api_key=api_key)

        # [AI GENERATED] 必須パラメーターが設定されることを検証
        assert client.api_key == api_key, f"Expected api_key '{api_key}', got '{client.api_key}'"

        # [AI GENERATED] デフォルト値が使用されることを検証
        assert client.base_url == expected_default_base_url, (
            f"Expected default base_url '{expected_default_base_url}', got '{client.base_url}'"
        )
        assert client.timeout == expected_default_timeout, (
            f"Expected default timeout {expected_default_timeout}, got {client.timeout}"
        )


class TestActionLogicAPI:
    """ActionLogicAPIのテストケース。

    ルール値の文字列化とHTTP POST操作を含む
    ActionLogicAPI機能を検証するためのテストケースが含まれています。
    """

    def setup_method(self) -> None:
        """各テストメソッドの前にテストフィクスチャを設定。

        SimpliseClientインスタンスを作成し、テストメソッドで使用する
        ActionLogicAPIインスタンスを抽出します。
        """
        self.client = SimpliseClient(api_key="test_api_key")
        self.action_logic = self.client.action_logic

    def test_action_logic_api_initialization(self) -> None:
        """ActionLogicAPI初期化をテスト。

        ActionLogicAPIが親SimpliseClientインスタンスへの
        参照で正しく初期化されることを検証します。
        """
        # [AI GENERATED] クライアント参照が正しく設定されることを検証
        assert self.action_logic.client is self.client, "ActionLogicAPI should have reference to parent client"

    def test_stringify_rule_values_with_basic_types(self) -> None:
        """基本データ型での_stringify_rule_valuesをテスト。

        _stringify_rule_valuesが基本型（整数、ブール値、浮動小数点）を
        正しく文字列表現に変換することを検証します。
        """
        # [AI GENERATED] 基本データ型でルールを作成
        rule = {"var": 42, "bool": True, "float": 3.14}

        # [AI GENERATED] ルール値を文字列化
        result = self.action_logic._stringify_rule_values(rule)  # noqa: SLF001

        # [AI GENERATED] すべての値が文字列に変換されることを検証
        expected = {"var": "42", "bool": "True", "float": "3.14"}
        assert result == expected, f"Expected {expected}, got {result}"

    def test_stringify_rule_values_with_nested_structures(self) -> None:
        """ネストしたデータ構造での_stringify_rule_valuesをテスト。

        _stringify_rule_valuesがネストした辞書とリストを正しく処理し、
        すべての非文字列値を再帰的に文字列に変換することを検証します。
        """
        # [AI GENERATED] ネスト構造でルールを作成
        rule = {
            "condition": {"==": [{"var": "age"}, 25]},
            "items": [1, 2, {"value": 3}],
        }

        # [AI GENERATED] ルール値を文字列化
        result = self.action_logic._stringify_rule_values(rule)  # noqa: SLF001

        # [AI GENERATED] ネスト値が正しく文字列化されることを検証
        expected = {
            "condition": {"==": [{"var": "age"}, "25"]},
            "items": ["1", "2", {"value": "3"}],
        }
        assert result == expected, f"Expected {expected}, got {result}"

    def test_stringify_rule_values_preserves_existing_strings(self) -> None:
        """既存の文字列を保持する_stringify_rule_valuesをテスト。

        _stringify_rule_valuesが文字列値を変更せずに保持し、
        非文字列値を文字列に変換することを検証します。
        """
        # [AI GENERATED] 文字列と非文字列値の混合でルールを作成
        rule = {"message": "hello", "count": 5}

        # [AI GENERATED] ルール値を文字列化
        result = self.action_logic._stringify_rule_values(rule)  # noqa: SLF001

        # [AI GENERATED] 文字列が保持され、数値が変換されることを検証
        expected = {"message": "hello", "count": "5"}
        assert result == expected, f"Expected {expected}, got {result}"

    @patch("requests.post")
    def test_post_request_success_with_input_data(self, mock_post: Mock) -> None:
        """入力データを含む成功したPOSTリクエストをテスト。

        postメソッドがルールと入力データの両方を含むHTTPリクエストを
        正しく送信し、成功時にレスポンステキストを返すことを検証します。
        """
        # [AI GENERATED] 成功したリクエストのためのモックレスポンスを設定
        mock_response = Mock()
        mock_response.text = "success"
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        rule: JsonLogicRule = {"var": "test"}
        input_data = {"key": "value"}

        # [AI GENERATED] POSTリクエストを送信
        result = self.action_logic.post(rule, input_data)

        # [AI GENERATED] 成功レスポンスを検証
        assert result == "success", f"Expected 'success', got '{result}'"

        # [AI GENERATED] POSTリクエストが正確に一度呼ばれることを検証
        mock_post.assert_called_once()

        # [AI GENERATED] リクエストパラメーターを検証
        call_args = mock_post.call_args
        assert call_args[1]["headers"]["Authorization"] == "Bearer test_api_key", (
            "Authorization header should contain correct API key"
        )
        assert "action" in call_args[1]["files"], "Request should include action file"
        assert "input" in call_args[1]["files"], "Request should include input file"

    @patch("requests.post")
    def test_post_request_without_input_data(self, mock_post: Mock) -> None:
        """入力データなしのPOSTリクエストをテスト。

        入力データが提供されない場合に、postメソッドがリクエストを正しく処理し、
        アクションファイルのみを送信することを検証します。
        """
        # [AI GENERATED] 成功したリクエストのためのモックレスポンスを設定
        mock_response = Mock()
        mock_response.text = "success"
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        rule: JsonLogicRule = {"var": "test"}

        # [AI GENERATED] 入力データなしでPOSTリクエストを送信
        result = self.action_logic.post(rule)

        # [AI GENERATED] 成功レスポンスを検証
        assert result == "success", f"Expected 'success', got '{result}'"

        # [AI GENERATED] リクエストにアクションファイルのみが含まれ、入力ファイルが含まれないことを検証
        call_args = mock_post.call_args
        assert "action" in call_args[1]["files"], "Request should include action file"
        assert "input" not in call_args[1]["files"], "Request should not include input file when no input data provided"


class TestAction:
    """Actionクラスのテストケース。

    ロジック実行とエラーハンドリング機能を含む
    Actionクラス機能を検証するためのテストケースが含まれています。
    """

    def setup_method(self) -> None:
        """各テストメソッドの前にテストフィクスチャを設定。

        SimpliseClientインスタンスを作成し、テストメソッドで使用する
        Actionインスタンスを抽出します。
        """
        self.client = SimpliseClient(api_key="test_api_key")
        self.action = self.client.action

    def test_action_initialization(self) -> None:
        """Action初期化をテスト。

        Actionが親SimpliseClientインスタンスへの
        参照で正しく初期化されることを検証します。
        """
        # [AI GENERATED] クライアント参照が正しく設定されることを検証
        assert self.action.client is self.client, "Action should have reference to parent client"

    @patch.object(ActionLogicAPI, "post")
    def test_execute_logic_with_data(self, mock_post: Mock) -> None:
        """入力データでのexecute_logicメソッドをテスト。

        execute_logicがActionLogicAPI.postに正しく委譲し、
        ルールとデータの両方が提供された場合に期待される結果を返すことを検証します。
        """
        # [AI GENERATED] モックレスポンスとテストデータを設定
        expected_result = "logic_result"
        mock_post.return_value = expected_result

        rule: JsonLogicRule = {"var": "test"}
        data = {"test": "value"}

        # [AI GENERATED] ルールとデータでロジックを実行
        result = self.action.execute_logic(rule, data)

        # [AI GENERATED] 正しい結果が返されることを検証
        assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

        # [AI GENERATED] ActionLogicAPI.postが正しいパラメーターで呼ばれることを検証
        mock_post.assert_called_once_with(rule, data)

    @patch.object(ActionLogicAPI, "post")
    def test_send_request_error_handling(self, mock_post: Mock) -> None:
        """_send_requestエラーハンドリングをテスト。

        _send_requestが基底のAPI呼び出しからの例外を適切に処理し、
        説明的なメッセージでRuntimeErrorを発生させることを検証します。
        """
        # [AI GENERATED] 例外を発生させるためのモックを設定
        error_message = "API Error"
        mock_post.side_effect = Exception(error_message)

        rule: JsonLogicRule = {"var": "test"}

        # [AI GENERATED] 正しいメッセージでRuntimeErrorが発生することを検証
        with pytest.raises(RuntimeError, match=f"Error sending request: {error_message}"):
            self.action._send_request(rule)  # noqa: SLF001
