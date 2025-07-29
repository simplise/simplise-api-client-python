"""# Simplise API Client Base

This module provides a client for interacting with the Simplise API.
"""

from typing import Any

import requests

from simplise_api_client_python.action import Operation
from simplise_api_client_python.type import (
    JsonLogicRule,
    JsonLogicRuleSafetyStr,
    JsonLogicValue,
    JsonLogicValueSafetyStr,
)


class ActionLogicAPI:
    """API client for action-logic endpoint."""

    def __init__(self, client: "SimpliseClient") -> None:
        """Initialize ActionLogicAPI with a reference to the client."""
        self.client = client

    def post(self, rule: JsonLogicRule) -> str:
        """Execute JsonLogic rule via action-logic POST endpoint.

        Args:
            rule (JsonLogicRule): The JsonLogic rule to execute

        Returns:
            str: The result from the API

        Raises:
            requests.HTTPError: If the API request fails
        """
        url = f"{self.client.base_url}/action-logic"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.client.api_key}"}

        safety_rule = self._stringify_rule_values(rule)
        response = requests.post(url, json=safety_rule, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()

    def _stringify_rule_values(self, rule: JsonLogicRule) -> JsonLogicRuleSafetyStr:
        """Convert all values in the rule to strings."""

        def stringify_value(value: JsonLogicValue) -> JsonLogicValueSafetyStr:
            if isinstance(value, (int, float, bool)):
                return str(value)
            if isinstance(value, list):
                return [str(v) for v in value]
            if isinstance(value, dict):
                return {k: str(v) for k, v in value.items()}
            return value

        return {k: stringify_value(v) for k, v in rule.items()}


class Action:
    def __init__(self, client: "SimpliseClient") -> None:
        """Initialize Action with a reference to the client."""
        self.client = client

    def execute(self, *operations: Operation) -> bool:
        """Execute library model operations.

        Args:
            *operations: Variable number of operation objects

        Returns:
            bool: True if operations executed successfully, False otherwise
        """
        # Convert operations to JSON Logic format
        rules = [op.to_dict() for op in operations]
        for rule in rules:
            if not isinstance(rule, dict):
                return False
            self._send_request(rule)
        return True

    def execute_logic(self, rule: JsonLogicRule, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Execute JsonLogic rule.

        Args:
            rule (JsonLogicRule): The JsonLogic rule to execute
            data (dict, optional): Input data for the rule

        Returns:
            Dict[str, Any]: The result of the rule execution
        """
        return self._send_request(rule, data)

    def _send_request(self, rule: JsonLogicRule, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Send request to Simplise API."""
        # Use the new ActionLogicAPI for actual requests
        try:
            result = self.client.action_logic.post(rule)
        except Exception as e:
            # Fallback to placeholder for error handling
            return {"result": "error", "rule": rule, "data": data, "error": str(e)}
        return {"result": result, "rule": rule, "data": data}


class SimpliseClient:
    """A client for interacting with the Simplise API.

    This class provides methods to interact with the Simplise API, including
    authentication, making requests, and handling responses.
    """

    def __init__(self, api_key: str) -> None:
        """Initializes the SimpliseClient with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the Simplise API.
        """
        self.api_key = api_key
        self.base_url = "https://api.usebootstrap.org"
        self.action = Action(self)
        self.action_logic = ActionLogicAPI(self)
