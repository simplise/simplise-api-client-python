"""This module provides utility functions and classes for handling operations"""

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

