"""# num

This module provides operations for numeric processing using JavaScript's standard floating-point number (Number type).

It is suitable for general numeric calculations, statistical processing, and comparison operations.
For high-precision calculations such as financial computations, consider using the `decimal` module instead.

Documents: https://api.usebootstrap.org/spec/doc/action/data/num.md
"""
# JavaScript標準の浮動小数点数（Number型）を使用した数値処理を提供します。
# 一般的な数値計算、統計処理、比較演算に適していますが、金融計算など高精度が必要な場合は decimal を使用してください。

import logging

from simplise_api_client.actions.utils import Operation
from simplise_api_client.type import OperationArg

logger = logging.getLogger(__name__)


def action_num(value: OperationArg) -> Operation:
    """Create a numeric operation.

    This operation converts the provided value to a number.

    Args:
        value (OperationArg): The value to convert to a number.

    Returns:
        Operation: An operation representing the numeric value.
    """
    logger.debug(f"Creating numeric operation for value: {value}")

    return Operation("num", value)

def action_num_add(*args: OperationArg) -> Operation:
    """Create a numeric addition operation.

    This operation adds multiple numeric values together.

    Args:
        *args (OperationArg): The numeric values to add.

    Returns:
        Operation: An operation representing the addition of the numeric values.
    """
    logger.debug(f"Creating numeric addition operation for values: {args}")

    return Operation("num.add", *args)

def action_num_sub(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric subtraction operation.

    This operation subtracts multiple numeric values.

    Args:
        arg1 (OperationArg): The first numeric value.
        arg2 (OperationArg): The second numeric value to subtract from the first.

    Returns:
        Operation: An operation representing the subtraction of the numeric values.
    """
    logger.debug(f"Creating numeric subtraction operation for values: {arg1}, {arg2}")

    return Operation("num.sub", arg1, arg2)

def action_num_mul(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric multiplication operation.

    This operation multiplies multiple numeric values together.

    Args:
        arg1 (OperationArg): The first numeric value.
        arg2 (OperationArg): The second numeric value to multiply with the first.

    Returns:
        Operation: An operation representing the multiplication of the numeric values.
    """
    logger.debug(f"Creating numeric multiplication operation for values: {arg1}, {arg2}")

    return Operation("num.mul", arg1, arg2)

def action_num_div(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric division operation.

    This operation divides multiple numeric values.

    Args:
        arg1 (OperationArg): The first numeric value (dividend).
        arg2 (OperationArg): The second numeric value (divisor).

    Returns:
        Operation: An operation representing the division of the numeric values.
    """
    logger.debug(f"Creating numeric division operation for values: {arg1}, {arg2}")

    return Operation("num.div", arg1, arg2)

def action_num_mod(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric modulo operation.

    This operation calculates the remainder of the division of multiple numeric values.

    Args:
        arg1 (OperationArg): The first numeric value (dividend).
        arg2 (OperationArg): The second numeric value (divisor).

    Returns:
        Operation: An operation representing the modulo of the numeric values.
    """
    logger.debug(f"Creating numeric modulo operation for values: {arg1}, {arg2}")

    return Operation("num.mod", arg1, arg2)

def action_num_gt(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric greater than operation.

    This operation checks if the first numeric value is greater than the second.

    Args:
        arg1 (OperationArg): The first numeric value.
        arg2 (OperationArg): The second numeric value to compare against.

    Returns:
        Operation: An operation representing the greater than comparison.
    """
    logger.debug(f"Creating numeric greater than operation for values: {arg1}, {arg2}")

    return Operation("num.gt", arg1, arg2)

def action_num_gte(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric greater than or equal operation.

    This operation checks if the first numeric value is greater than or equal to the second.

    Args:
        arg1 (OperationArg): The first numeric value to compare.
        arg2 (OperationArg): The second numeric value to compare against.

    Returns:
        Operation: An operation representing the greater than or equal comparison.
    """
    logger.debug(f"Creating numeric greater than or equal operation for values: {arg1}, {arg2}")

    return Operation("num.gte", arg1, arg2)

def action_num_lt(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric less than operation.

    This operation checks if the first numeric value is less than the second.

    Args:
        arg1 (OperationArg): The first numeric value to compare.
        arg2 (OperationArg): The second numeric value to compare against.

    Returns:
        Operation: An operation representing the less than comparison.
    """
    logger.debug(f"Creating numeric less than operation for values: {arg1}, {arg2}")

    return Operation("num.lt", arg1, arg2)

def action_num_lte(arg1: OperationArg, arg2: OperationArg) -> Operation:
    """Create a numeric less than or equal operation.

    This operation checks if the first numeric value is less than or equal to the second.

    Args:
        arg1 (OperationArg): The first numeric value to compare.
        arg2 (OperationArg): The second numeric value to compare against.

    Returns:
        Operation: An operation representing the less than or equal comparison.
    """
    logger.debug(f"Creating numeric less than or equal operation for values: {arg1}, {arg2}")

    return Operation("num.lte", arg1, arg2)

def action_num_max(*args: OperationArg) -> Operation:
    """Create a numeric maximum operation.

    This operation finds the maximum value among the provided numeric values.

    Args:
        *args (OperationArg): The numeric values to compare.

    Returns:
        Operation: An operation representing the maximum value.
    """
    logger.debug(f"Creating numeric maximum operation for values: {args}")

    return Operation("num.max", *args)

def action_num_min(*args: OperationArg) -> Operation:
    """Create a numeric minimum operation.

    This operation finds the minimum value among the provided numeric values.

    Args:
        *args (OperationArg): The numeric values to compare.

    Returns:
        Operation: An operation representing the minimum value.
    """
    logger.debug(f"Creating numeric minimum operation for values: {args}")

    return Operation("num.min", *args)

def action_num_between(
    check_value: OperationArg, lower_bound: OperationArg, upper_bound: OperationArg
) -> Operation:
    """Create a numeric between operation.

    This operation checks if the first numeric value is between the second and third values.

    Args:
        check_value (OperationArg): The numeric value to check.
        lower_bound (OperationArg): The lower bound of the range.
        upper_bound (OperationArg): The upper bound of the range.

    Returns:
        Operation: An operation representing the between comparison.
    """
    logger.debug(f"Creating numeric between operation for values: {check_value}, {lower_bound}, {upper_bound}")

    return Operation("num.between", check_value, lower_bound, upper_bound)
