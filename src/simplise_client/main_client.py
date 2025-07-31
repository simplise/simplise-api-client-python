"""Main client for Simplise API (equivalent to executer.ts)."""

from typing import Any

from .action_client import ActionClient
from .auth_client import AuthClient
from .http_client import HttpClient
from .types import ApiConfig, ApiResponse, HttpMethod, RetryConfig


class SimpliseClient:
    """Main Simplise API client."""

    def __init__(
        self,
        api_key: str,
        base_url: str | None = None,
        timeout: int | None = None,
        retry_config: RetryConfig | None = None,
    ) -> None:
        """Initialize Simplise client.

        Args:
            api_key (str): API key for authentication
            base_url (str | None): Base URL for the API
            timeout (int | None): Request timeout in seconds
            retry_config (RetryConfig | None): Retry configuration for HTTP requests
        """
        # [AI GENERATED] Initialize main client with all sub-clients
        config: ApiConfig = {
            "api_key": api_key,
            "base_url": base_url,
            "timeout": timeout,
            "retry_config": retry_config
            or {
                "max_retries": 3,
                "max_retry_delay": 5,
                "enable_retry_for_429": True,
                "enable_retry_for_202": True,
            },
        }
        self.http_client = HttpClient(config)
        self.auth = AuthClient(self.http_client)
        self.action = ActionClient(self.http_client)

    async def custom_request(
        self,
        endpoint: str,
        method: HttpMethod = HttpMethod.GET,
        data: Any | None = None,
        headers: dict[str, str] | None = None,
    ) -> ApiResponse:
        """Make custom endpoint request.

        Args:
            endpoint: API endpoint
            method: HTTP method
            data: Request data
            headers: Request headers

        Returns:
            API response
        """
        # [AI GENERATED] Custom request method for arbitrary endpoints
        match method:
            case HttpMethod.GET:
                return await self.http_client.get(endpoint, headers)
            case HttpMethod.POST:
                return await self.http_client.post(endpoint, data, headers)
            case HttpMethod.PUT:
                return await self.http_client.put(endpoint, data, headers)
            case HttpMethod.DELETE:
                return await self.http_client.delete(endpoint, headers)
            case _:
                return await self.http_client.request(
                    endpoint, {"method": method, "body": str(data) if data else None, "headers": headers}
                )

    # async def health_check(self) -> ApiResponse[dict[str, str]]:
    #     """Health check endpoint.
    #
    #     Returns:
    #         API response with health status
    #     """
    #     # [AI GENERATED] Health check endpoint
    #     return await self.http_client.get("/health")
    #
    # async def get_api_info(self) -> ApiResponse:
    #     """Get API information.
    #
    #     Returns:
    #         API response with API info
    #     """
    #     # [AI GENERATED] API info endpoint
    #     return await self.http_client.get("/info")
