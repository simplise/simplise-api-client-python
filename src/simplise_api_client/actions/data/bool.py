"""# bool

This module provides a boolean operation for the Simplise API client.

This operation generates a boolean value (true or false) based on the provided input.
It supports conversion of various types such as numbers, strings, arrays, and objects to boolean values.

Documents: https://api.usebootstrap.org/spec/doc/action/data/bool.md
"""
# 論理値（true または false）を生成します
# 任意の値を論理値に変換します。数値、文字列、配列、オブジェクトなど様々な型から論理値への変換をサポートします。

import logging

from simplise_api_client.actions.utils import Operation
from simplise_api_client.type import OperationArg

logger = logging.getLogger(__name__)


def action_bool(value: OperationArg) -> Operation:
    """Create a boolean operation.

    This operation evaluates the truthiness of the provided value.

    Args:
        value (OperationArg): The value to evaluate as a boolean.

    Returns:
        Operation: An operation representing the boolean value.
    """
    logger.debug(f"Creating boolean operation for value: {value}")

    return Operation("bool", value)

