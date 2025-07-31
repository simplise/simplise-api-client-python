import warnings

from simplise_api_client.actions import Operation
from simplise_api_client.type import OperationArg


def action_decimal_add(*args: OperationArg) -> Operation:
    """Create a decimal addition action.

    小数点の加算操作を作成する。

    .. deprecated::
        Use Action.Decimal.add() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Decimal.add() instead.
    warnings.warn(
        "action_decimal_add is deprecated. Use Action.Decimal.add() instead.", DeprecationWarning, stacklevel=2
    )
    return Operation("decimal.add", *args)


def action_decimal_mul(*args: OperationArg) -> Operation:
    """Create a decimal multiplication action.

    小数点の乗算操作を作成する。

    .. deprecated::
        Use Action.Decimal.mul() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Decimal.mul() instead.
    warnings.warn(
        "action_decimal_mul is deprecated. Use Action.Decimal.mul() instead.", DeprecationWarning, stacklevel=2
    )
    return Operation("decimal.mul", *args)


def action_decimal_sub(*args: OperationArg) -> Operation:
    """Create a decimal subtraction action.

    小数点の減算操作を作成する。

    .. deprecated::
        Use Action.Decimal.sub() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Decimal.sub() instead.
    warnings.warn(
        "action_decimal_sub is deprecated. Use Action.Decimal.sub() instead.", DeprecationWarning, stacklevel=2
    )
    return Operation("decimal.sub", *args)


def action_decimal_div(*args: OperationArg) -> Operation:
    """Create a decimal division action.

    小数点の除算操作を作成する。

    .. deprecated::
        Use Action.Decimal.div() instead.
    """
    # [AI GENERATED] This function is deprecated. Use Action.Decimal.div() instead.
    warnings.warn(
        "action_decimal_div is deprecated. Use Action.Decimal.div() instead.", DeprecationWarning, stacklevel=2
    )
    return Operation("decimal.div", *args)


class Decimal:
    """Decimal arithmetic operations.

    小数点演算操作を提供するクラス。

    .. deprecated::
        Use Action.Decimal instead.
    """

    @staticmethod
    def add(*args: OperationArg) -> Operation:
        """Create a decimal addition action.

        小数点の加算操作を作成する。

        .. deprecated::
            Use Action.Decimal.add() instead.
        """
        # [AI GENERATED] This method is deprecated. Use Action.Decimal.add() instead.
        warnings.warn("Decimal.add is deprecated. Use Action.Decimal.add() instead.", DeprecationWarning, stacklevel=2)
        return Operation("decimal.add", *args)

    @staticmethod
    def mul(*args: OperationArg) -> Operation:
        """Create a decimal multiplication action.

        小数点の乗算操作を作成する。

        .. deprecated::
            Use Action.Decimal.mul() instead.
        """
        # [AI GENERATED] This method is deprecated. Use Action.Decimal.mul() instead.
        warnings.warn("Decimal.mul is deprecated. Use Action.Decimal.mul() instead.", DeprecationWarning, stacklevel=2)
        return Operation("decimal.mul", *args)

    @staticmethod
    def sub(*args: OperationArg) -> Operation:
        """Create a decimal subtraction action.

        小数点の減算操作を作成する。

        .. deprecated::
            Use Action.Decimal.sub() instead.
        """
        # [AI GENERATED] This method is deprecated. Use Action.Decimal.sub() instead.
        warnings.warn("Decimal.sub is deprecated. Use Action.Decimal.sub() instead.", DeprecationWarning, stacklevel=2)
        return Operation("decimal.sub", *args)

    @staticmethod
    def div(*args: OperationArg) -> Operation:
        """Create a decimal division action.

        小数点の除算操作を作成する。

        .. deprecated::
            Use Action.Decimal.div() instead.
        """
        # [AI GENERATED] This method is deprecated. Use Action.Decimal.div() instead.
        warnings.warn("Decimal.div is deprecated. Use Action.Decimal.div() instead.", DeprecationWarning, stacklevel=2)
        return Operation("decimal.div", *args)
