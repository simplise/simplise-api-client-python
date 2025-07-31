from simplise_api_client.actions.utils import Operation
from simplise_api_client.type import OperationArg


def action_decimal_add(*args: OperationArg) -> Operation:
    """Create a decimal addition action.

    小数点の加算操作を作成する。
    """
    return Operation("decimal.add", *args)


def action_decimal_mul(*args: OperationArg) -> Operation:
    """Create a decimal multiplication action.

    小数点の乗算操作を作成する。
    """
    return Operation("decimal.mul", *args)


def action_decimal_sub(*args: OperationArg) -> Operation:
    """Create a decimal subtraction action.

    小数点の減算操作を作成する。
    """
    return Operation("decimal.sub", *args)


def action_decimal_div(*args: OperationArg) -> Operation:
    """Create a decimal division action.

    小数点の除算操作を作成する。
    """
    return Operation("decimal.div", *args)
