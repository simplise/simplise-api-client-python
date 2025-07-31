"""Action operations for Simplise API client.

This module provides operation builders for the Simplise API.
"""

from simplise_api_client.actions.numeric.decimal import (
    action_decimal_add,
    action_decimal_div,
    action_decimal_mul,
    action_decimal_sub,
)
from simplise_api_client.actions.utils import Operation, action_input, action_obj

__all__ = [
    "Operation",
    "action_decimal_add",
    "action_decimal_div",
    "action_decimal_mul",
    "action_decimal_sub",
    "action_input",
    "action_obj",
]
