"""# Simplise API Client Base

This module provides a client for interacting with the Simplise API.
"""

import json
from typing import Any, cast

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

    def execute(self, operation: Operation, data: dict[str, str]) -> dict[str, Any]:
        """Execute library model operation.

        Args:
            operation (Operation): The operation object to execute
            data (dict[str, str]): The input data for the operation

        Returns:
            dict[str, Any]: The result of the operation execution
        """
        # Convert operations to JSON Logic format
        return self._send_request(operation.to_dict(), data)

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
                input_keys = [v.replace(check_name, "").strip() for v in value if isinstance(v, str)]
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
                processed_items = []
                for item in value:
                    if isinstance(item, dict) and all(isinstance(k, str) for k in item):
                        # item を JsonLogicRule として再帰処理
                        processed_items.append(self._replace_action_input(cast("JsonLogicRule", item), data))
                    else:
                        processed_items.append(item)
                rule[key] = processed_items
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
