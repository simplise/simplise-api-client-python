"""# Simplise API Client Base

This module provides a client for interacting with the Simplise API.
"""

import json
import logging
from typing import Any, cast

import requests
from pydantic import ValidationError

from simplise_api_client.actions import Operation
from simplise_api_client.models import (
    ActionExecuteRequest,
    ActionExecuteResponse,
    ActionLogicRequest,
    ActionLogicResponse,
    JsonLogicExecuteRequest,
    JsonLogicExecuteResponse,
)
from simplise_api_client.type import (
    JsonLogicRule,
    JsonLogicRuleSafetyStr,
    JsonLogicValue,
    JsonLogicValueSafetyStr,
)

logger = logging.getLogger(__name__)


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
            ValidationError: If the request data validation fails
        """
        # [AI GENERATED] リクエストデータをPydanticモデルで検証
        try:
            request_model = ActionLogicRequest(rule=rule, input_data=input_data)
        except ValidationError:
            logger.exception("Request validation failed")
            raise

        url = f"{self.client.base_url}/action-logic"
        headers = {"Authorization": f"Bearer {self.client.api_key}"}

        safety_rule = self._stringify_rule_values(request_model.rule)

        # Prepare multipart form data
        files = {"action": (None, json.dumps(safety_rule), "application/json")}

        if request_model.input_data:
            safety_data = self._stringify_rule_values(request_model.input_data)
            files["input"] = (None, json.dumps(safety_data), "application/json")

        response = requests.post(url, files=files, headers=headers, timeout=self.client.timeout)
        response.raise_for_status()

        # [AI GENERATED] レスポンスデータをPydanticモデルで検証
        try:
            response_model = ActionLogicResponse(result=response.text)
        except ValidationError:
            logger.exception("Response validation failed")
            raise
        else:
            return response_model.result

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

    def execute(self, operation: Operation, data: dict[str, str] | None = None) -> str:
        """Execute library model operation.

        Args:
            operation (Operation): The operation object to execute
            data (dict[str, str] | None): The input data for the operation

        Returns:
            str: The result of the operation execution

        Raises:
            ValidationError: If the request data validation fails
        """
        # [AI GENERATED] リクエストデータをPydanticモデルで検証
        try:
            request_model = ActionExecuteRequest(operation_data=operation.to_dict(), input_data=data)
        except ValidationError:
            logger.exception("Request validation failed for execute")
            raise

        # Convert operations to JSON Logic format
        result = self._send_request(request_model.operation_data, request_model.input_data)

        # [AI GENERATED] レスポンスデータをPydanticモデルで検証
        try:
            response_model = ActionExecuteResponse(result=result)
        except ValidationError:
            logger.exception("Response validation failed for execute")
            raise
        else:
            return response_model.result

    def execute_logic(self, rule: JsonLogicRule, data: dict[str, Any] | None = None) -> str:
        """Execute JsonLogic rule.

        Args:
            rule (JsonLogicRule): The JsonLogic rule to execute
            data (dict, optional): Input data for the rule

        Returns:
            str: The result of the rule execution

        Raises:
            ValidationError: If the request data validation fails
        """
        # [AI GENERATED] リクエストデータをPydanticモデルで検証
        try:
            request_model = JsonLogicExecuteRequest(rule=rule, data=data)
        except ValidationError:
            logger.exception("Request validation failed for execute_logic")
            raise

        # rule = self._replace_action_input(rule, data)
        result = self._send_request(request_model.rule, request_model.data)

        # [AI GENERATED] レスポンスデータをPydanticモデルで検証
        try:
            response_model = JsonLogicExecuteResponse(result=result)
        except ValidationError:
            logger.exception("Response validation failed for execute_logic")
            raise
        else:
            return response_model.result

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

    def _send_request(self, rule: JsonLogicRule, data: dict[str, Any] | None = None) -> str:
        """Send request to Simplise API."""
        # Use the new ActionLogicAPI for actual requests
        try:
            result = self.client.action_logic.post(rule, data)
        except Exception as e:
            # Fallback to placeholder for error handling
            err_msg = f"Error sending request: {e}"
            raise RuntimeError(err_msg) from e
        return result


class SimpliseClient:
    """A client for interacting with the Simplise API.

    This class provides methods to interact with the Simplise API, including
    authentication, making requests, and handling responses.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.usebootstrap.org", timeout: float = 30.0) -> None:
        """Initializes the SimpliseClient with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the Simplise API.
            base_url (str): The base URL for the Simplise API.
            timeout (float): The timeout for API requests in seconds.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.action = Action(self)
        self.action_logic = ActionLogicAPI(self)
