"""Action operations for Simplise API client.

This module provides operation builders for the Simplise API.
"""

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


class DecimalOperations:
    """Decimal arithmetic operations."""

    @staticmethod
    def add(*args: OperationArg) -> Operation:
        """Create a decimal addition operation."""
        return Operation("decimal.add", *args)

    @staticmethod
    def mul(*args: OperationArg) -> Operation:
        """Create a decimal multiplication operation."""
        return Operation("decimal.mul", *args)

    @staticmethod
    def sub(*args: OperationArg) -> Operation:
        """Create a decimal subtraction operation."""
        return Operation("decimal.sub", *args)

    @staticmethod
    def div(*args: OperationArg) -> Operation:
        """Create a decimal division operation."""
        return Operation("decimal.div", *args)


def input_ref(key: str) -> Operation:
    """Create an input reference.

    Args:
        key (str): The input key to reference

    Returns:
        Operation: An operation that references the input key
    """
    return Operation("input", key)


# Create instances for easy access
decimal = DecimalOperations()
