"""data.bool モジュールのテスト。

このモジュールには、action_bool関数の包括的なテストケースが含まれています。
bool操作の正しい動作を検証します。
"""

from simplise_api_client.actions import action_input
from simplise_api_client.actions.data.bool import action_bool
from simplise_api_client.actions.utils import Operation


class TestActionBool:
    """action_bool関数のテストケース。

    bool値作成の正しい動作、Operation インスタンスの作成、
    様々な引数タイプの処理を検証するためのテストケースが含まれています。
    """

    def test_action_bool_creates_correct_operation(self) -> None:
        """action_bool関数が正しいOperationを作成することをテスト。

        action_boolがbool操作に対して正しい演算子と
        引数を持つOperationを作成することを検証します。
        """
        # [AI GENERATED] テスト値を定義
        test_value = "test_string"

        # [AI GENERATED] bool操作を作成
        result = action_bool(test_value)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "bool", f"Expected operator 'bool', got '{result.operator}'"
        assert result.args == (test_value,), f"Expected args {(test_value,)}, got {result.args}"

    def test_action_bool_with_true_value(self) -> None:
        """真値でのaction_boolをテスト。

        action_boolがTrue値を正しく処理できることを検証します。
        """
        # [AI GENERATED] 真値でbool操作を作成
        test_true = True
        result = action_bool(test_true)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "bool", f"Expected operator 'bool', got '{result.operator}'"
        assert result.args == (test_true,), f"Expected args {(test_true,)}, got {result.args}"

    def test_action_bool_with_false_value(self) -> None:
        """偽値でのaction_boolをテスト。

        action_boolがFalse値を正しく処理できることを検証します。
        """
        # [AI GENERATED] 偽値でbool操作を作成
        test_false = False
        result = action_bool(test_false)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "bool", f"Expected operator 'bool', got '{result.operator}'"
        assert result.args == (test_false,), f"Expected args {(test_false,)}, got {result.args}"

    def test_action_bool_with_numeric_value(self) -> None:
        """数値でのaction_boolをテスト。

        action_boolが数値を正しく処理できることを検証します。
        """
        # [AI GENERATED] 数値でbool操作を作成
        test_number = 42
        result = action_bool(test_number)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "bool", f"Expected operator 'bool', got '{result.operator}'"
        assert result.args == (test_number,), f"Expected args {(test_number,)}, got {result.args}"

    def test_action_bool_with_zero_value(self) -> None:
        """ゼロ値でのaction_boolをテスト。

        action_boolがゼロ値を正しく処理できることを検証します。
        """
        # [AI GENERATED] ゼロ値でbool操作を作成
        test_zero = 0
        result = action_bool(test_zero)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "bool", f"Expected operator 'bool', got '{result.operator}'"
        assert result.args == (test_zero,), f"Expected args {(test_zero,)}, got {result.args}"

    def test_action_bool_with_string_value(self) -> None:
        """文字列でのaction_boolをテスト。

        action_boolが文字列を正しく処理できることを検証します。
        """
        # [AI GENERATED] 文字列でbool操作を作成
        test_string = "hello"
        result = action_bool(test_string)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "bool", f"Expected operator 'bool', got '{result.operator}'"
        assert result.args == (test_string,), f"Expected args {(test_string,)}, got {result.args}"

    def test_action_bool_with_empty_string(self) -> None:
        """空文字列でのaction_boolをテスト。

        action_boolが空文字列を正しく処理できることを検証します。
        """
        # [AI GENERATED] 空文字列でbool操作を作成
        test_empty = ""
        result = action_bool(test_empty)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "bool", f"Expected operator 'bool', got '{result.operator}'"
        assert result.args == (test_empty,), f"Expected args {(test_empty,)}, got {result.args}"

    def test_action_bool_with_operation_argument(self) -> None:
        """Operation引数でのaction_boolをテスト。

        action_boolがOperation インスタンスを引数として受け取り、
        それを正しく処理できることを検証します。
        """
        # [AI GENERATED] Operation引数を作成
        input_op = action_input("some_value")

        # [AI GENERATED] Operation引数でaction_boolを実行
        result = action_bool(input_op)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "bool", f"Expected operator 'bool', got '{result.operator}'"
        assert result.args == (input_op,), "Expected args to contain the input Operation"

    def test_action_bool_to_dict_conversion_with_simple_value(self) -> None:
        """単純な値でのaction_boolのto_dict変換をテスト。

        action_boolが作成したOperationが正しく
        辞書形式に変換されることを検証します。
        """
        # [AI GENERATED] 単純な値でaction_boolを作成
        test_value = "test"
        result = action_bool(test_value)

        # [AI GENERATED] 辞書に変換
        result_dict = result.to_dict()

        # [AI GENERATED] 正しい辞書構造を検証
        expected = {"bool": [test_value]}
        assert result_dict == expected, f"Expected {expected}, got {result_dict}"

    def test_action_bool_to_dict_conversion_with_operation_argument(self) -> None:
        """Operation引数でのaction_boolのto_dict変換をテスト。

        action_boolがネストしたOperation引数を正しく辞書に変換できることを検証します。
        """
        # [AI GENERATED] Operation引数を作成
        input_op = action_input("dynamic_value")
        result = action_bool(input_op)

        # [AI GENERATED] 辞書に変換
        result_dict = result.to_dict()

        # [AI GENERATED] ネスト構造が正しく表現されることを検証
        expected = {"bool": [{"input": ["dynamic_value"]}]}
        assert result_dict == expected, f"Expected {expected}, got {result_dict}"
