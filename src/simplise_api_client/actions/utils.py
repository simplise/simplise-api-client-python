"""This module provides utility functions and classes for handling operations"""

import warnings

from simplise_api_client.actions.numeric.decimal import Decimal
from simplise_api_client.type import JsonLogicRule, OperationArg


class Operation:
    """Base class for all operations."""

    def __init__(self, operator: str, *args: OperationArg) -> None:
        self.operator = operator
        self.args = args

    def to_dict(self) -> JsonLogicRule:
        """Convert operation to dictionary format."""
        # Convert arguments to dictionary format if they are Operation instances
        args = [arg.to_dict() if isinstance(arg, Operation) else arg for arg in self.args]
        return {self.operator: list(args)}


class Action:
    """Unified action class providing all operation types.

    すべての操作タイプを提供する統合アクションクラス。
    """
    decimal = Decimal()

    # Data operations
    class Data:
        """Data processing operations.

        データ処理操作を提供するクラス。
        """

        @staticmethod
        def bool(value: OperationArg) -> Operation:
            """Create a boolean operation.

            論理値操作を作成する。

            Args:
                value: The value to evaluate as a boolean.

            Returns:
                Operation: A boolean operation.
            """
            # [AI GENERATED] Create boolean operation
            return Operation("bool", value)

        @staticmethod
        def input(key: str) -> Operation:
            """Create an input operation.

            入力操作を作成する。

            Args:
                key: The input key to reference.

            Returns:
                Operation: An input operation.
            """
            # [AI GENERATED] Create input operation
            return Operation("input", key)

        @staticmethod
        def obj(key: str, value: str) -> dict[str, str]:
            """Create an object dictionary.

            オブジェクト辞書を作成する。

            Args:
                key: The object key.
                value: The object value.

            Returns:
                dict: An object dictionary.
            """
            # [AI GENERATED] Create object dictionary
            return {key: value}

    # Numeric operations
    class Num:
        """Numeric operations.

        数値操作を提供するクラス。
        """

        @staticmethod
        def add(*args: OperationArg) -> Operation:
            """Create a numeric addition operation.

            数値加算操作を作成する。

            Args:
                *args: Operation arguments for numeric addition.

            Returns:
                Operation: A numeric addition operation.
            """
            # [AI GENERATED] Create numeric addition operation
            return Operation("num.add", *args)

        @staticmethod
        def sub(arg1: OperationArg, arg2: OperationArg) -> Operation:
            """Create a numeric subtraction operation.

            数値減算操作を作成する。

            Args:
                arg1: The first operand.
                arg2: The second operand.

            Returns:
                Operation: A numeric subtraction operation.
            """
            # [AI GENERATED] Create numeric subtraction operation
            return Operation("num.sub", arg1, arg2)

        @staticmethod
        def mul(arg1: OperationArg, arg2: OperationArg) -> Operation:
            """Create a numeric multiplication operation.

            数値乗算操作を作成する。

            Args:
                arg1: The first operand.
                arg2: The second operand.

            Returns:
                Operation: A numeric multiplication operation.
            """
            # [AI GENERATED] Create numeric multiplication operation
            return Operation("num.mul", arg1, arg2)

        @staticmethod
        def div(arg1: OperationArg, arg2: OperationArg) -> Operation:
            """Create a numeric division operation.

            数値除算操作を作成する。

            Args:
                arg1: The first operand.
                arg2: The second operand.

            Returns:
                Operation: A numeric division operation.
            """
            # [AI GENERATED] Create numeric division operation
            return Operation("num.div", arg1, arg2)

        @staticmethod
        def mod(arg1: OperationArg, arg2: OperationArg) -> Operation:
            """Create a numeric modulo operation.

            数値剰余操作を作成する。

            Args:
                arg1: The first operand.
                arg2: The second operand.

            Returns:
                Operation: A numeric modulo operation.
            """
            # [AI GENERATED] Create numeric modulo operation
            return Operation("num.mod", arg1, arg2)

        @staticmethod
        def gt(arg1: OperationArg, arg2: OperationArg) -> Operation:
            """Create a numeric greater than operation.

            数値大なり比較操作を作成する。

            Args:
                arg1: The first operand.
                arg2: The second operand.

            Returns:
                Operation: A numeric greater than operation.
            """
            # [AI GENERATED] Create numeric greater than operation
            return Operation("num.gt", arg1, arg2)

        @staticmethod
        def gte(arg1: OperationArg, arg2: OperationArg) -> Operation:
            """Create a numeric greater than or equal operation.

            数値大なりイコール比較操作を作成する。

            Args:
                arg1: The first operand.
                arg2: The second operand.

            Returns:
                Operation: A numeric greater than or equal operation.
            """
            # [AI GENERATED] Create numeric greater than or equal operation
            return Operation("num.gte", arg1, arg2)

        @staticmethod
        def lt(arg1: OperationArg, arg2: OperationArg) -> Operation:
            """Create a numeric less than operation.

            数値小なり比較操作を作成する。

            Args:
                arg1: The first operand.
                arg2: The second operand.

            Returns:
                Operation: A numeric less than operation.
            """
            # [AI GENERATED] Create numeric less than operation
            return Operation("num.lt", arg1, arg2)

        @staticmethod
        def lte(arg1: OperationArg, arg2: OperationArg) -> Operation:
            """Create a numeric less than or equal operation.

            数値小なりイコール比較操作を作成する。

            Args:
                arg1: The first operand.
                arg2: The second operand.

            Returns:
                Operation: A numeric less than or equal operation.
            """
            # [AI GENERATED] Create numeric less than or equal operation
            return Operation("num.lte", arg1, arg2)

        @staticmethod
        def max(*args: OperationArg) -> Operation:
            """Create a numeric maximum operation.

            数値最大値操作を作成する。

            Args:
                *args: Operation arguments for finding maximum.

            Returns:
                Operation: A numeric maximum operation.
            """
            # [AI GENERATED] Create numeric maximum operation
            return Operation("num.max", *args)

        @staticmethod
        def min(*args: OperationArg) -> Operation:
            """Create a numeric minimum operation.

            数値最小値操作を作成する。

            Args:
                *args: Operation arguments for finding minimum.

            Returns:
                Operation: A numeric minimum operation.
            """
            # [AI GENERATED] Create numeric minimum operation
            return Operation("num.min", *args)

        @staticmethod
        def between(value: OperationArg, min_val: OperationArg, max_val: OperationArg) -> Operation:
            """Create a numeric between operation.

            数値範囲チェック操作を作成する。

            Args:
                value: The value to check.
                min_val: The minimum value.
                max_val: The maximum value.

            Returns:
                Operation: A numeric between operation.
            """
            # [AI GENERATED] Create numeric between operation
            return Operation("num.between", value, min_val, max_val)

    # Decimal operations
    class Decimal:
        """Decimal arithmetic operations.

        小数点演算操作を提供するクラス。
        """

        @staticmethod
        def add(*args: OperationArg) -> Operation:
            """Create a decimal addition action.

            小数点の加算操作を作成する。

            Args:
                *args: Operation arguments for decimal addition.

            Returns:
                Operation: A decimal addition operation.
            """
            # [AI GENERATED] Create decimal addition operation
            return Operation("decimal.add", *args)

        @staticmethod
        def mul(*args: OperationArg) -> Operation:
            """Create a decimal multiplication action.

            小数点の乗算操作を作成する。

            Args:
                *args: Operation arguments for decimal multiplication.

            Returns:
                Operation: A decimal multiplication operation.
            """
            # [AI GENERATED] Create decimal multiplication operation
            return Operation("decimal.mul", *args)

        @staticmethod
        def sub(*args: OperationArg) -> Operation:
            """Create a decimal subtraction action.

            小数点の減算操作を作成する。

            Args:
                *args: Operation arguments for decimal subtraction.

            Returns:
                Operation: A decimal subtraction operation.
            """
            # [AI GENERATED] Create decimal subtraction operation
            return Operation("decimal.sub", *args)

        @staticmethod
        def div(*args: OperationArg) -> Operation:
            """Create a decimal division action.

            小数点の除算操作を作成する。

            Args:
                *args: Operation arguments for decimal division.

            Returns:
                Operation: A decimal division operation.
            """
            # [AI GENERATED] Create decimal division operation
            return Operation("decimal.div", *args)

    # Logic operations
    class Logic:
        """Logic operations.

        論理操作を提供するクラス。
        """

        @staticmethod
        def and_op(*conditions: OperationArg) -> Operation:
            """Create a logical AND operation.

            論理積操作を作成する。

            Args:
                *conditions: Conditions to evaluate.

            Returns:
                Operation: A logical AND operation.
            """
            # [AI GENERATED] Create logical AND operation
            processed_conditions = []
            for condition in conditions:
                # もしconditionがbool値の場合、action_bool変換する
                processed_condition = Operation("bool", condition) if type(condition) is bool else condition
                processed_conditions.append(processed_condition)

            return Operation("and", *processed_conditions)


# Deprecated functions for backward compatibility
def action_bool(value: OperationArg) -> Operation:
    """Create a boolean operation.

    論理値操作を作成する。

    .. deprecated::
        Use Action.Data.bool() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Data.bool() instead.
    warnings.warn("action_bool is deprecated. Use Action.Data.bool() instead.", DeprecationWarning, stacklevel=2)
    return Operation("bool", value)


def action_input(key: str) -> Operation:
    """Create an input operation.

    入力操作を作成する。

    .. deprecated::
        Use Action.Data.input() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Data.input() instead.
    warnings.warn("action_input is deprecated. Use Action.Data.input() instead.", DeprecationWarning, stacklevel=2)
    return Operation("input", key)


def action_obj(key: str, value: str) -> dict[str, str]:
    """Create an object dictionary.

    オブジェクト辞書を作成する。

    .. deprecated::
        Use Action.Data.obj() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Data.obj() instead.
    warnings.warn("action_obj is deprecated. Use Action.Data.obj() instead.", DeprecationWarning, stacklevel=2)
    return {key: value}


def action_and(*conditions: OperationArg) -> Operation:
    """Create a logical AND operation.

    論理積操作を作成する。

    .. deprecated::
        Use Action.Logic.and_op() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Logic.and_op() instead.
    warnings.warn("action_and is deprecated. Use Action.Logic.and_op() instead.", DeprecationWarning, stacklevel=2)
    processed_conditions = []
    for condition in conditions:
        # もしconditionがbool値の場合、action_bool変換する
        processed_condition = Operation("bool", condition) if type(condition) is bool else condition
        processed_conditions.append(processed_condition)

    return Operation("and", *processed_conditions)


# Numeric deprecated functions
def action_num_add(*args: OperationArg) -> Operation:
    """Create a numeric addition operation.

    数値加算操作を作成する。

    .. deprecated::
        Use Action.Num.add() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.add() instead.
    warnings.warn("action_num_add is deprecated. Use Action.Num.add() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.add", *args)


def action_num_sub(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric subtraction operation.

    数値減算操作を作成する。

    .. deprecated::
        Use Action.Num.sub() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.sub() instead.
    warnings.warn("action_num_sub is deprecated. Use Action.Num.sub() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.sub", arg1, arg2)


def action_num_mul(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric multiplication operation.

    数値乗算操作を作成する。

    .. deprecated::
        Use Action.Num.mul() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.mul() instead.
    warnings.warn("action_num_mul is deprecated. Use Action.Num.mul() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.mul", arg1, arg2)


def action_num_div(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric division operation.

    数値除算操作を作成する。

    .. deprecated::
        Use Action.Num.div() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.div() instead.
    warnings.warn("action_num_div is deprecated. Use Action.Num.div() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.div", arg1, arg2)


def action_num_mod(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric modulo operation.

    数値剰余操作を作成する。

    .. deprecated::
        Use Action.Num.mod() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.mod() instead.
    warnings.warn("action_num_mod is deprecated. Use Action.Num.mod() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.mod", arg1, arg2)


def action_num_gt(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric greater than operation.

    数値大なり比較操作を作成する。

    .. deprecated::
        Use Action.Num.gt() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.gt() instead.
    warnings.warn("action_num_gt is deprecated. Use Action.Num.gt() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.gt", arg1, arg2)


def action_num_gte(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric greater than or equal operation.

    数値大なりイコール比較操作を作成する。

    .. deprecated::
        Use Action.Num.gte() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.gte() instead.
    warnings.warn("action_num_gte is deprecated. Use Action.Num.gte() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.gte", arg1, arg2)


def action_num_lt(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric less than operation.

    数値小なり比較操作を作成する。

    .. deprecated::
        Use Action.Num.lt() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.lt() instead.
    warnings.warn("action_num_lt is deprecated. Use Action.Num.lt() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.lt", arg1, arg2)


def action_num_lte(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric less than or equal operation.

    数値小なりイコール比較操作を作成する。

    .. deprecated::
        Use Action.Num.lte() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.lte() instead.
    warnings.warn("action_num_lte is deprecated. Use Action.Num.lte() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.lte", arg1, arg2)


def action_num_max(*args: OperationArg) -> Operation:
    """Create a numeric maximum operation.

    数値最大値操作を作成する。

    .. deprecated::
        Use Action.Num.max() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.max() instead.
    warnings.warn("action_num_max is deprecated. Use Action.Num.max() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.max", *args)


def action_num_min(*args: OperationArg) -> Operation:
    """Create a numeric minimum operation.

    数値最小値操作を作成する。

    .. deprecated::
        Use Action.Num.min() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.min() instead.
    warnings.warn("action_num_min is deprecated. Use Action.Num.min() instead.", DeprecationWarning, stacklevel=2)
    return Operation("num.min", *args)


def action_num_between(value: OperationArg, min_val: OperationArg, max_val: OperationArg) -> Operation:
    """Create a numeric between operation.

    数値範囲チェック操作を作成する。

    .. deprecated::
        Use Action.Num.between() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Num.between() instead.
    warnings.warn(
        "action_num_between is deprecated. Use Action.Num.between() instead.", DeprecationWarning, stacklevel=2
    )
    return Operation("num.between", value, min_val, max_val)
