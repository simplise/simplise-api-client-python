from simplise_api_client.actions.utils import Operation
from simplise_api_client.type import OperationArg


def action_decimal_add(*args: OperationArg) -> Operation:
    """Create a decimal addition action."""
    return Operation("decimal.add", *args)


def action_decimal_mul(*args: OperationArg) -> Operation:
    """Create a decimal multiplication action."""
    return Operation("decimal.mul", *args)


def action_decimal_sub(*args: OperationArg) -> Operation:
    """Create a decimal subtraction action."""
    return Operation("decimal.sub", *args)


def action_decimal_div(*args: OperationArg) -> Operation:
    """Create a decimal division action."""
    return Operation("decimal.div", *args)
