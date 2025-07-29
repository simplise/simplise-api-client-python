"""# Simplise API Client Base

This module provides a client for interacting with the Simplise API.
"""

import json
from typing import Any

import requests

from simplise_api_client.actions import Operation
from simplise_api_client.type import (
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

    def post(self, rule: JsonLogicRule, input_data: dict[str, Any] | None = None) -> str:
        """Execute JsonLogic rule via action-logic POST endpoint.

        Args:
            rule (JsonLogicRule): The JsonLogic rule to execute
            input_data (dict, optional): Input data to be sent as form data

        Returns:
            str: The result from the API

        Raises:
            requests.HTTPError: If the API request fails
        """
        url = f"{self.client.base_url}/action-logic"
        headers = {"Authorization": f"Bearer {self.client.api_key}"}

        safety_rule = self._stringify_rule_values(rule)

        # Prepare multipart form data
        files = {"action": (None, json.dumps(safety_rule), "application/json")}

        if input_data:
            safety_data = self._stringify_rule_values(input_data)
            files["input"] = (None, json.dumps(safety_data), "application/json")

        response = requests.post(url, files=files, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()

    def _stringify_rule_values(self, rule: JsonLogicRule) -> JsonLogicRuleSafetyStr:
        """Convert all values in the rule to strings."""

        # def stringify_value(value: JsonLogicValue) -> Any:
        #     if isinstance(value, (int, float, bool)):
        #         return str(value)
        #     if isinstance(value, list):
        #         return [stringify_value(v) for v in value]  # 再帰的に処理
        #     if isinstance(value, dict):
        #         return {k: stringify_value(v) for k, v in value.items()}  # 再帰的に処理
        #     return value
        def stringify_value(
            value: JsonLogicValue,
        ) -> JsonLogicValueSafetyStr:
            if isinstance(value, (int, float, bool)):
                return str(value)
            if isinstance(value, list):
                return [stringify_value(v) for v in value]
            if isinstance(value, dict):
                return {k: stringify_value(v) for k, v in value.items()}
            return value  # str型の場合はそのまま返す

        if isinstance(rule, dict):
            return {k: stringify_value(v) for k, v in rule.items()}
        return rule


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
        # rule = self._replace_action_input(rule, data)
        return self._send_request(rule, data)

    # ruleの中に"{"action_input": "[<input_key>]"}" がある場合は、
    # dataの中の{"<input_key>": "<input_value>"}から値を取得して
    # {"input": "<input_value>"}に置き換える
    def _replace_action_input(self, rule: JsonLogicRule, data: dict[str, Any] | None) -> JsonLogicRule:
        """Replace action_input references in the rule with actual data values."""
        check_name = "action_input"
        for key, value in list(rule.items()):
            if isinstance(value, list) and check_name in key:
                input_keys = [value.replace(check_name, "").strip() for value in value if isinstance(value, str)]
                if data is None:
                    err_msg = "Data must be provided to replace action_input"
                    raise ValueError(err_msg)
                for input_key in input_keys:
                    if input_key in data:
                        rule["input"] = rule.pop(check_name)
                        rule["input"] = data[input_key]
                    else:
                        err_msg = f"Input key '{input_key}' not found in data"
                        raise ValueError(err_msg)
            elif isinstance(value, list):
                rule[key] = [
                    self._replace_action_input(item, data) if isinstance(item, dict) else item for item in value
                ]
        return rule

    def _send_request(self, rule: JsonLogicRule, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Send request to Simplise API."""
        # Use the new ActionLogicAPI for actual requests
        try:
            result = self.client.action_logic.post(rule, data)
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
