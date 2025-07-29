"""# Simplise API Client

This module provides a client for interacting with the Simplise API.
"""

from simplise_api_client.actions import (
    action_decimal_add,
    action_decimal_div,
    action_decimal_mul,
    action_decimal_sub,
    action_input,
    action_obj,
)
from simplise_api_client.base import SimpliseClient

__all__ = [
    "SimpliseClient",
    "action_decimal_add",
    "action_decimal_div",
    "action_decimal_mul",
    "action_decimal_sub",
    "action_input",
    "action_obj",
]
