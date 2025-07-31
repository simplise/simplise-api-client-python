"""Action client for Simplise API."""

import json
import logging

from .http_client import HttpClient
from .types import ApiResponse, JsonLogicRule, JsonValue

logger = logging.getLogger(__name__)


class ActionClient:
    """Action client for Simplise API."""

    def __init__(self, http_client: HttpClient) -> None:
        """Initialize action client.

        Args:
            http_client: HTTP client instance
        """
        # [AI GENERATED] Initialize action client with HTTP client
        self.http_client = http_client

    async def execute_url(self, endpoint: str) -> ApiResponse:
        """Execute action using URL parameters.

        Args:
            endpoint: Action endpoint with parameters

        Returns:
            API response
        """
        # [AI GENERATED] Execute action with URL parameter format
        return await self.http_client.get(f"/action?{endpoint}")

    async def execute_with_text(self, endpoint: str, text: str) -> ApiResponse:
        """Execute action with text body.

        Args:
            endpoint: Action endpoint with parameters
            text: Text data

        Returns:
            API response
        """
        # [AI GENERATED] Execute action with text body
        return await self.http_client.post_text(f"/action?{endpoint}", text)

    async def execute_with_json(self, endpoint: str, data: JsonValue) -> ApiResponse:
        """Execute action with JSON body.

        Args:
            endpoint: Action endpoint with parameters
            data: JSON data

        Returns:
            API response
        """
        # [AI GENERATED] Execute action with JSON body
        return await self.http_client.post(f"/action?{endpoint}", data)

    async def execute_logic(self, rule: JsonLogicRule, input_data: JsonValue | None = None) -> ApiResponse:
        """Execute JsonLogic rule.

        Args:
            rule: JsonLogic rule to execute
            input_data: Optional input data

        Returns:
            API response
        """
        # [AI GENERATED] Execute JsonLogic rule with optional input data
        if input_data is not None:
            # Send as multipart/form-data when input data is provided
            logger.info("Sending multipart/form-data:")
            logger.info(f"Action: {json.dumps(rule, indent=2)}")
            logger.info(f"Input: {json.dumps(input_data, indent=2)}")

            # Create form data with proper content types
            form_data = {
                "action": (None, json.dumps(rule), "application/json"),
                "input": (None, json.dumps(input_data), "application/json"),
            }

            return await self.http_client.post_form("/action-logic", form_data)
        # Send as JSON when no input data
        logger.info(json.dumps(rule, indent=2))
        return await self.http_client.post("/action-logic", rule)

    async def execute_query(self, query_rule: str) -> ApiResponse:
        """Execute query rule.

        Args:
            query_rule: Query rule string

        Returns:
            API response
        """
        # [AI GENERATED] Execute query rule via GET request
        return await self.http_client.get(f"/logic?{query_rule}")

    async def execute(self, *functions: JsonLogicRule) -> ApiResponse:
        """Execute function(s) using library model.

        Args:
            *functions: JsonLogic rules to execute

        Returns:
            API response
        """
        # [AI GENERATED] Execute single or multiple functions with sequence composition
        if len(functions) == 1:
            return await self.execute_logic(functions[0])

        # Create composite rule for multiple functions
        composite_rule: JsonLogicRule = {"sequence": list(functions)}

        return await self.execute_logic(composite_rule)

    # async def execute_batch(
    #     self,
    #     actions: list[dict[str, Any]]
    # ) -> ApiResponse[list[Any]]:
    #     """Execute multiple actions in batch.
    #
    #     Args:
    #         actions: List of action configurations
    #
    #     Returns:
    #         API response with batch results
    #     """
    #     # [AI GENERATED] Execute multiple actions concurrently
    #     import asyncio
    #
    #     async def execute_single_action(action: dict[str, Any]) -> Any:
    #         if "endpoint" in action:
    #             response = await self.execute_url(action["endpoint"])
    #         elif "rule" in action:
    #             response = await self.execute_logic(
    #                 action["rule"],
    #                 action.get("input_data")
    #             )
    #         else:
    #             raise ValueError("Action must have either endpoint or rule")
    #
    #         return response.get("data")
    #
    #     try:
    #         tasks = [execute_single_action(action) for action in actions]
    #         results = await asyncio.gather(*tasks)
    #
    #         return {
    #             "success": True,
    #             "data": results,
    #             "status": 200
    #         }
    #
    #     except Exception as e:
    #         return {
    #             "success": False,
    #             "error": str(e),
    #             "status": 500
    #         }
