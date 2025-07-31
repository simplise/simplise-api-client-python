"""actionsモジュールのテスト。

このモジュールには、actionsモジュールの包括的なテストケースが含まれています。
Operation クラスの機能とユーティリティ関数をテストします。
"""

from simplise_api_client.actions import (
    Operation,
    action_decimal_add,
    action_decimal_div,
    action_decimal_mul,
    action_decimal_sub,
    action_input,
    action_obj,
)


class TestOperation:
    """Operation クラスのテストケース。

    Operation クラスの初期化、辞書変換、ネストした操作の処理を
    検証するためのテストケースが含まれています。
    """

    def test_operation_initialization_with_valid_arguments(self) -> None:
        """有効な引数でのOperation初期化をテスト。

        Operation インスタンスが演算子と引数で正しく初期化され、
        これらの値が適切に保存されることを検証します。
        """
        # [AI GENERATED] 特定の演算子と引数でOperationを作成
        operator = "test_op"
        arg1, arg2 = "arg1", "arg2"

        # [AI GENERATED] Operation インスタンスを初期化
        op = Operation(operator, arg1, arg2)

        # [AI GENERATED] 演算子と引数が正しく保存されていることを検証
        assert op.operator == operator, f"Expected operator '{operator}', got '{op.operator}'"
        assert op.args == (arg1, arg2), f"Expected args {(arg1, arg2)}, got {op.args}"

    def test_to_dict_conversion_with_simple_arguments(self) -> None:
        """単純な引数でのto_dictメソッドをテスト。

        単純な引数タイプ（数値）を使用する場合に、Operationが
        正しく辞書形式に変換できることを検証します。
        """
        # [AI GENERATED] 単純な数値引数でoperationを作成
        op = Operation("add", 1, 2)

        # [AI GENERATED] operationを辞書に変換
        result = op.to_dict()

        # [AI GENERATED] 正しい辞書構造を検証
        expected = {"add": [1, 2]}
        assert result == expected, f"Expected {expected}, got {result}"

    def test_to_dict_conversion_with_nested_operations(self) -> None:
        """ネストした操作でのto_dictメソッドをテスト。

        Operationがネストした操作を処理し、それらを正しく
        ネストした辞書構造に変換できることを検証します。
        """
        # [AI GENERATED] ネストした操作を作成
        nested_op = Operation("sub", 5, 3)
        op = Operation("add", nested_op, 2)

        # [AI GENERATED] 辞書に変換
        result = op.to_dict()

        # [AI GENERATED] ネスト構造が正しく表現されていることを検証
        expected = {"add": [{"sub": [5, 3]}, 2]}
        assert result == expected, f"Expected {expected}, got {result}"

    def test_to_dict_conversion_with_mixed_argument_types(self) -> None:
        """混合引数タイプでのto_dictメソッドをテスト。

        Operationが数値、ネストした操作、文字列を含む
        混合引数タイプを単一の操作で処理できることを検証します。
        """
        # [AI GENERATED] 混合引数タイプでoperationを作成
        nested_op = Operation("input", "value")
        op = Operation("decimal.add", 10, nested_op, "text")

        # [AI GENERATED] 辞書に変換
        result = op.to_dict()

        # [AI GENERATED] すべての引数タイプが正しく処理されることを検証
        expected = {"decimal.add": [10, {"input": ["value"]}, "text"]}
        assert result == expected, f"Expected {expected}, got {result}"


class TestActionUtilities:
    """アクションユーティリティ関数のテストケース。

    Operation インスタンスを作成するアクションユーティリティ関数と
    その他のヘルパー関数を検証するためのテストケースが含まれています。
    """

    def test_action_input_creates_correct_operation(self) -> None:
        """action_input関数が正しいOperationを作成することをテスト。

        action_input関数が入力操作に対して正しい演算子と引数を持つ
        Operation インスタンスを作成することを検証します。
        """
        # [AI GENERATED] テストキーを定義
        test_key = "test_key"

        # [AI GENERATED] 入力操作を作成
        result = action_input(test_key)

        # [AI GENERATED] Operation インスタンスが正しく作成されることを検証
        assert isinstance(result, Operation), f"Expected Operation instance, got {type(result)}"
        assert result.operator == "input", f"Expected operator 'input', got '{result.operator}'"
        assert result.args == (test_key,), f"Expected args {(test_key,)}, got {result.args}"

        # [AI GENERATED] 辞書変換が正しく動作することを検証
        expected_dict = {"input": [test_key]}
        actual_dict = result.to_dict()
        assert actual_dict == expected_dict, f"Expected {expected_dict}, got {actual_dict}"

    def test_action_obj_creates_correct_dictionary(self) -> None:
        """action_obj関数が正しい辞書を作成することをテスト。

        action_obj関数が指定されたキー・バリューペアで
        辞書を作成することを検証します。
        """
        # [AI GENERATED] テストキーと値を定義
        key, value = "name", "John"

        # [AI GENERATED] オブジェクト辞書を作成
        result = action_obj(key, value)

        # [AI GENERATED] 正しい辞書が作成されることを検証
        expected = {key: value}
        assert result == expected, f"Expected {expected}, got {result}"
        assert isinstance(result, dict), f"Expected dict, got {type(result)}"


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
