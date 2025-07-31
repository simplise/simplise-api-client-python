"""logic.add モジュールのテスト。

このモジュールには、action_and関数の包括的なテストケースが含まれています。
論理AND演算の動作を検証します。
"""

from simplise_api_client.actions import action_input
from simplise_api_client.actions.logic.add import action_and
from simplise_api_client.actions.utils import Operation


class TestActionAnd:
    """action_and関数のテストケース。

    論理AND演算の正しい動作、Operation インスタンスの作成、
    様々な引数タイプの処理を検証するためのテストケースが含まれています。
    """

    def test_action_and_creates_correct_operation(self) -> None:
        """action_and関数が正しいOperationを作成することをテスト。

        action_andが論理AND操作に対して正しい演算子と
        引数を持つOperationを作成することを検証します。
        """
        # [AI GENERATED] テスト引数を定義
        test_true = True
        test_false = False
        args = (test_true, test_false, test_true)

        # [AI GENERATED] 論理AND操作を作成
        result = action_and(*args)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "and", f"Expected operator 'and', got '{result.operator}'"

        # [AI GENERATED] bool値がaction_boolに変換されていることを検証
        expected_count = 3
        assert len(result.args) == expected_count, f"Expected {expected_count} args, got {len(result.args)}"

        for i, actual in enumerate(result.args):
            assert isinstance(actual, Operation), f"Arg {i} should be Operation, got {type(actual)}"
            assert actual.operator == "bool", f"Arg {i} should have operator 'bool', got '{actual.operator}'"

    def test_action_and_with_operation_arguments(self) -> None:
        """Operation引数でのaction_andをテスト。

        action_andがOperation インスタンスを引数として受け取り、
        それらを正しく処理できることを検証します。
        """
        # [AI GENERATED] Operation引数を作成
        input_op1 = action_input("condition1")
        input_op2 = action_input("condition2")

        # [AI GENERATED] Operation引数でaction_andを実行
        result = action_and(input_op1, input_op2)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "and", f"Expected operator 'and', got '{result.operator}'"
        assert result.args == (input_op1, input_op2), "Expected args to be unchanged Operation instances"

    def test_action_and_with_mixed_arguments(self) -> None:
        """混合引数タイプでのaction_andをテスト。

        action_andがbool値とOperation インスタンスの混合引数を
        正しく処理できることを検証します。
        """
        # [AI GENERATED] 混合引数を作成
        input_op = action_input("condition")
        bool_value = True

        # [AI GENERATED] 混合引数でaction_andを実行
        result = action_and(input_op, bool_value)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "and", f"Expected operator 'and', got '{result.operator}'"
        # [AI GENERATED] Operation引数で行う
        expected_arg_count = 2
        assert len(result.args) == expected_arg_count, f"Expected {expected_arg_count} args, got {len(result.args)}"

        # [AI GENERATED] 最初の引数はそのままのOperation
        assert result.args[0] is input_op, "First arg should be the original Operation"

        # [AI GENERATED] 2番目の引数はaction_boolに変換されたbool値
        assert isinstance(result.args[1], Operation), "Second arg should be converted to Operation"
        assert result.args[1].operator == "bool", "Second arg should have operator 'bool'"

    def test_action_and_to_dict_conversion(self) -> None:
        """action_andのto_dict変換をテスト。

        action_andが作成したOperationが正しく
        辞書形式に変換されることを検証します。
        """
        # [AI GENERATED] 単純なbool引数でaction_andを作成
        test_true = True
        test_false = False
        result = action_and(test_true, test_false)

        # [AI GENERATED] 辞書に変換
        result_dict = result.to_dict()

        # [AI GENERATED] 正しい辞書構造を検証
        expected = {"and": [{"bool": [True]}, {"bool": [False]}]}
        assert result_dict == expected, f"Expected {expected}, got {result_dict}"

    def test_action_and_with_single_condition(self) -> None:
        """単一条件でのaction_andをテスト。

        action_andが単一の条件を正しく処理できることを検証します。
        """
        # [AI GENERATED] 単一条件でaction_andを実行
        test_true = True
        result = action_and(test_true)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "and", f"Expected operator 'and', got '{result.operator}'"
        assert len(result.args) == 1, f"Expected 1 arg, got {len(result.args)}"

    def test_action_and_with_no_conditions(self) -> None:
        """条件なしでのaction_andをテスト。

        action_andが引数なしで呼び出された場合の動作を検証します。
        """
        # [AI GENERATED] 引数なしでaction_andを実行
        result = action_and()

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "and", f"Expected operator 'and', got '{result.operator}'"
        assert len(result.args) == 0, f"Expected 0 args, got {len(result.args)}"

    def test_action_and_with_multiple_conditions(self) -> None:
        """複数条件でのaction_andをテスト。

        action_andが多数の条件を正しく処理できることを検証します。
        """
        # [AI GENERATED] 複数条件を作成
        conditions = [True, False, True, False, True]

        # [AI GENERATED] 複数条件でaction_andを実行
        result = action_and(*conditions)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "and", f"Expected operator 'and', got '{result.operator}'"
        assert len(result.args) == len(conditions), f"Expected {len(conditions)} args, got {len(result.args)}"

    def test_action_and_with_nested_operations(self) -> None:
        """ネストした操作でのaction_andをテスト。

        action_andがネストしたOperation引数を正しく処理し、
        複雑な論理構造を作成できることを検証します。
        """
        # [AI GENERATED] ネストした操作を作成
        test_true = True
        test_false = False
        nested_and = action_and(test_true, test_false)
        input_op = action_input("external_condition")

        # [AI GENERATED] ネストした操作を含むaction_andを実行
        result = action_and(nested_and, input_op)

        # [AI GENERATED] ネスト構造が正しく作成されることを検証
        expected_dict = {"and": [{"and": [{"bool": [True]}, {"bool": [False]}]}, {"input": ["external_condition"]}]}
        actual_dict = result.to_dict()
        assert actual_dict == expected_dict, f"Expected {expected_dict}, got {actual_dict}"
