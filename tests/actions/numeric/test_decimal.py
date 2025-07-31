"""numeric.decimal モジュールのテスト。

このモジュールには、小数演算関数の包括的なテストケースが含まれています。
加算、乗算、減算、除算を検証します。
"""

from simplise_api_client.actions import (
    action_decimal_add,
    action_decimal_div,
    action_decimal_mul,
    action_decimal_sub,
    action_input,
)
from simplise_api_client.actions.utils import Operation


class TestDecimalActions:
    """小数演算アクション関数のテストケース。

    加算、乗算、減算、除算を含む小数算術演算を
    検証するためのテストケースが含まれています。
    """

    def test_action_decimal_add_creates_correct_operation(self) -> None:
        """action_decimal_add関数が正しいOperationを作成することをテスト。

        action_decimal_addが小数加算操作に対して正しい演算子と
        引数を持つOperationを作成することを検証します。
        """
        # [AI GENERATED] テスト引数を定義
        args = (1, 2, 3)

        # [AI GENERATED] 小数加算操作を作成
        result = action_decimal_add(*args)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "decimal.add", f"Expected operator 'decimal.add', got '{result.operator}'"
        assert result.args == args, f"Expected args {args}, got {result.args}"

        # [AI GENERATED] 辞書変換が正しく動作することを検証
        expected_dict = {"decimal.add": list(args)}
        actual_dict = result.to_dict()
        assert actual_dict == expected_dict, f"Expected {expected_dict}, got {actual_dict}"

    def test_action_decimal_mul_creates_correct_operation(self) -> None:
        """action_decimal_mul関数が正しいOperationを作成することをテスト。

        action_decimal_mulが小数乗算操作に対して正しい演算子と
        引数を持つOperationを作成することを検証します。
        """
        # [AI GENERATED] テスト引数を定義
        args = (2, 3)

        # [AI GENERATED] 小数乗算操作を作成
        result = action_decimal_mul(*args)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "decimal.mul", f"Expected operator 'decimal.mul', got '{result.operator}'"
        assert result.args == args, f"Expected args {args}, got {result.args}"

        # [AI GENERATED] 辞書変換が正しく動作することを検証
        expected_dict = {"decimal.mul": list(args)}
        actual_dict = result.to_dict()
        assert actual_dict == expected_dict, f"Expected {expected_dict}, got {actual_dict}"

    def test_action_decimal_sub_creates_correct_operation(self) -> None:
        """action_decimal_sub関数が正しいOperationを作成することをテスト。

        action_decimal_subが小数減算操作に対して正しい演算子と
        引数を持つOperationを作成することを検証します。
        """
        # [AI GENERATED] テスト引数を定義
        args = (10, 3)

        # [AI GENERATED] 小数減算操作を作成
        result = action_decimal_sub(*args)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "decimal.sub", f"Expected operator 'decimal.sub', got '{result.operator}'"
        assert result.args == args, f"Expected args {args}, got {result.args}"

        # [AI GENERATED] 辞書変換が正しく動作することを検証
        expected_dict = {"decimal.sub": list(args)}
        actual_dict = result.to_dict()
        assert actual_dict == expected_dict, f"Expected {expected_dict}, got {actual_dict}"

    def test_action_decimal_div_creates_correct_operation(self) -> None:
        """action_decimal_div関数が正しいOperationを作成することをテスト。

        action_decimal_divが小数除算操作に対して正しい演算子と
        引数を持つOperationを作成することを検証します。
        """
        # [AI GENERATED] テスト引数を定義
        args = (10, 2)

        # [AI GENERATED] 小数除算操作を作成
        result = action_decimal_div(*args)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "decimal.div", f"Expected operator 'decimal.div', got '{result.operator}'"
        assert result.args == args, f"Expected args {args}, got {result.args}"

        # [AI GENERATED] 辞書変換が正しく動作することを検証
        expected_dict = {"decimal.div": list(args)}
        actual_dict = result.to_dict()
        assert actual_dict == expected_dict, f"Expected {expected_dict}, got {actual_dict}"

    def test_decimal_operations_with_operation_arguments(self) -> None:
        """Operation引数での小数演算をテスト。

        小数演算がOperation インスタンスを引数として受け取り、
        辞書変換でネスト構造を正しく処理できることを検証します。
        """
        # [AI GENERATED] 入力操作を作成し、小数演算と組み合わせ
        input_op = action_input("amount")

        # [AI GENERATED] Operation引数で小数加算を作成
        result = action_decimal_add(input_op, 10)

        # [AI GENERATED] ネスト構造が正しく作成されることを検証
        expected_dict = {"decimal.add": [{"input": ["amount"]}, 10]}
        actual_dict = result.to_dict()
        assert actual_dict == expected_dict, f"Expected {expected_dict}, got {actual_dict}"

    def test_complex_nested_decimal_operations(self) -> None:
        """複雑なネストした小数演算をテスト。

        複数の小数演算をネストして (5 + 3) * 2 のような
        複雑な数学式を作成できることを検証します。
        """
        # [AI GENERATED] (5 + 3) * 2 を表すネスト操作を作成
        add_op = action_decimal_add(5, 3)
        mul_op = action_decimal_mul(add_op, 2)

        # [AI GENERATED] 辞書表現に変換
        result = mul_op.to_dict()

        # [AI GENERATED] 複雑なネスト構造が正しく表現されることを検証
        expected = {"decimal.mul": [{"decimal.add": [5, 3]}, 2]}
        assert result == expected, f"Expected {expected}, got {result}"

    def test_decimal_operations_with_zero_values(self) -> None:
        """ゼロ値での小数演算をテスト。

        小数演算がゼロ値を正しく処理できることを検証します。
        """
        # [AI GENERATED] ゼロ値での演算をテスト
        result_add = action_decimal_add(0, 5)
        result_mul = action_decimal_mul(0, 5)
        result_sub = action_decimal_sub(5, 0)
        result_div = action_decimal_div(0, 5)

        # [AI GENERATED] 各演算が正しく作成されることを検証
        assert result_add.operator == "decimal.add"
        assert result_mul.operator == "decimal.mul"
        assert result_sub.operator == "decimal.sub"
        assert result_div.operator == "decimal.div"

        # [AI GENERATED] 引数が正しく保存されることを検証
        assert result_add.args == (0, 5)
        assert result_mul.args == (0, 5)
        assert result_sub.args == (5, 0)
        assert result_div.args == (0, 5)

    def test_decimal_operations_with_negative_values(self) -> None:
        """負の値での小数演算をテスト。

        小数演算が負の値を正しく処理できることを検証します。
        """
        # [AI GENERATED] 負の値での演算をテスト
        result_add = action_decimal_add(-5, 3)
        result_mul = action_decimal_mul(-2, 4)
        result_sub = action_decimal_sub(10, -3)
        result_div = action_decimal_div(-8, 2)

        # [AI GENERATED] 各演算が正しく作成されることを検証
        assert result_add.operator == "decimal.add"
        assert result_mul.operator == "decimal.mul"
        assert result_sub.operator == "decimal.sub"
        assert result_div.operator == "decimal.div"

        # [AI GENERATED] 引数が正しく保存されることを検証
        assert result_add.args == (-5, 3)
        assert result_mul.args == (-2, 4)
        assert result_sub.args == (10, -3)
        assert result_div.args == (-8, 2)

    def test_decimal_operations_with_multiple_arguments(self) -> None:
        """複数引数での小数演算をテスト。

        小数演算が複数の引数を正しく処理できることを検証します。
        """
        # [AI GENERATED] 複数引数での加算をテスト
        args = (1, 2, 3, 4, 5)
        result = action_decimal_add(*args)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "decimal.add", f"Expected operator 'decimal.add', got '{result.operator}'"
        assert result.args == args, f"Expected args {args}, got {result.args}"

        # [AI GENERATED] 辞書変換が正しく動作することを検証
        expected_dict = {"decimal.add": list(args)}
        actual_dict = result.to_dict()
        assert actual_dict == expected_dict, f"Expected {expected_dict}, got {actual_dict}"
