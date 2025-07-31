"""Type definitions for Simplise API Client."""

from enum import Enum
from typing import Any, Protocol, TypedDict

# HTTP status code constants
HTTP_ACCEPTED = 202
HTTP_TOO_MANY_REQUESTS = 429


class HttpMethod(str, Enum):
    """HTTP methods."""

    # [AI GENERATED] HTTP method enumeration
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class RetryConfig(TypedDict, total=False):
    """Retry configuration for HTTP requests."""

    # [AI GENERATED] Configuration for request retry behavior
    max_retries: int
    max_retry_delay: int  # seconds
    enable_retry_for_429: bool
    enable_retry_for_202: bool


class ApiConfig(TypedDict):
    """API client configuration."""

    # [AI GENERATED] Main configuration for API client
    api_key: str
    base_url: str | None
    timeout: int | None  # seconds
    retry_config: RetryConfig | None


class ApiResponse(TypedDict, total=False):
    """API response structure."""

    # [AI GENERATED] Standard API response format
    success: bool
    data: Any | None
    error: str | None
    status: int | None
    headers: dict[str, str] | None


class ErrorResponse(TypedDict):
    """Error response structure."""

    # [AI GENERATED] Error response format
    error: str
    status: int
    message: str | None


class RequestOptions(TypedDict, total=False):
    """HTTP request options."""

    # [AI GENERATED] Options for HTTP requests
    method: HttpMethod
    headers: dict[str, str]
    body: str | bytes | None
    timeout: int
    retry_config: RetryConfig


class AuthSession(TypedDict, total=False):
    """Authentication session data."""

    # [AI GENERATED] Authentication session information
    session_cookie: str
    csrf_token: str | None


class LoginCredentials(TypedDict, total=False):
    """Login credentials."""

    # [AI GENERATED] User login information
    username: str
    password: str
    turnstile_token: str | None


# Type aliases
JsonPrimitive = str | int | float | bool | None
JsonArray = list["JsonValue"]
JsonObject = dict[str, "JsonValue"]
JsonValue = JsonPrimitive | JsonArray | JsonObject

JsonLogicRule = dict[str, list["JsonLogicRule"]] | str | int | float
ActionParams = dict[str, list["ActionParams"]] | JsonPrimitive


class ApiError(Exception):
    """API error exception."""

    def __init__(self, status: int, response: ErrorResponse, message: str | None = None) -> None:
        """Initialize API error.

        Args:
            status: HTTP status code
            response: Error response data
            message: Optional error message
        """
        # [AI GENERATED] Initialize API error with status and response
        super().__init__(message or response["error"])
        self.status = status
        self.response = response


class HttpClientProtocol(Protocol):
    """Protocol for HTTP client interface."""

    async def request(self, endpoint: str, options: RequestOptions | None = None) -> ApiResponse:
        """Make HTTP request.

        Args:
            endpoint: API endpoint
            options: Request options

        Returns:
            API response
        """
        # [AI GENERATED] Protocol method for HTTP requests
        ...

    async def get(self, endpoint: str, headers: dict[str, str] | None = None) -> ApiResponse:
        """Make GET request.

        Args:
            endpoint: API endpoint
            headers: Request headers

        Returns:
            API response
        """
        # [AI GENERATED] Protocol method for GET requests
        ...

    async def post(
        self, endpoint: str, data: JsonValue | None = None, headers: dict[str, str] | None = None
    ) -> ApiResponse:
        """Make POST request.

        Args:
            endpoint: API endpoint
            data: Request data
            headers: Request headers

        Returns:
            API response
        """
        # [AI GENERATED] Protocol method for POST requests
        ...
