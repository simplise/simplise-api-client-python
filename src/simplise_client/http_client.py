"""HTTP client for Simplise API."""

import asyncio
import json
import logging
from datetime import datetime
from typing import Any

import httpx

from .types import (
    HTTP_ACCEPTED,
    HTTP_TOO_MANY_REQUESTS,
    ApiConfig,
    ApiError,
    ApiResponse,
    ErrorResponse,
    HttpMethod,
    JsonValue,
    RequestOptions,
    RetryConfig,
)

logger = logging.getLogger(__name__)


class HttpClient:
    """HTTP client with retry functionality."""

    def __init__(self, config: ApiConfig) -> None:
        """Initialize HTTP client.

        Args:
            config: API configuration
        """
        # [AI GENERATED] Initialize HTTP client with configuration and retry settings
        self.config: ApiConfig = {
            "api_key": config["api_key"],
            "base_url": config.get("base_url", "https://api.usebootstrap.org"),
            "timeout": config.get("timeout", 5),
            "retry_config": config.get("retry_config"),
        }

        self.retry_config: RetryConfig = {
            "max_retries": 3,
            "max_retry_delay": 30,  # 30 seconds
            "enable_retry_for_429": True,
            "enable_retry_for_202": True,
        }

        if self.config["retry_config"]:
            self.retry_config.update(self.config["retry_config"])

    def _parse_retry_after(self, retry_after: str | None) -> int:
        """Parse Retry-After header value.

        Args:
            retry_after: Retry-After header value

        Returns:
            Delay in seconds
        """
        # [AI GENERATED] Parse Retry-After header to get delay time
        if not retry_after:
            return 1  # Default 1 second

        try:
            # Try parsing as integer (seconds)
            seconds = int(retry_after)
            return min(seconds, self.retry_config["max_retry_delay"])
        except ValueError:
            pass

        try:
            # Try parsing as HTTP-date format
            date = datetime.fromisoformat(retry_after)
            delay = int((date - datetime.now()).total_seconds())
            return max(0, min(delay, self.retry_config["max_retry_delay"]))
        except (ValueError, TypeError):
            pass

        return 1  # Default 1 second if parsing fails

    def _should_retry(self, status: int | None, attempt: int) -> bool:
        """Check if request should be retried.

        Args:
            status: HTTP status code
            attempt: Current attempt number

        Returns:
            Whether to retry the request
        """
        # [AI GENERATED] Determine if request should be retried based on status and attempt count
        if attempt >= self.retry_config["max_retries"]:
            return False

        if status == HTTP_TOO_MANY_REQUESTS and self.retry_config["enable_retry_for_429"]:
            return True

        return status == HTTP_ACCEPTED and self.retry_config["enable_retry_for_202"]

    async def _perform_request(self, endpoint: str, options: RequestOptions | None = None) -> ApiResponse:
        """Perform actual HTTP request.

        Args:
            endpoint: API endpoint
            options: Request options

        Returns:
            API response with headers
        """
        # [AI GENERATED] Execute HTTP request with proper error handling and response parsing
        if options is None:
            options = {}

        url = f"{self.config['base_url']}{endpoint}"
        method = options.get("method", HttpMethod.GET)
        headers = {"Authorization": f"Bearer {self.config['api_key']}", **(options.get("headers", {}))}
        timeout = options.get("timeout", self.config["timeout"])

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.request(
                    method=method.value,
                    url=url,
                    headers=headers,
                    content=options.get("body"),
                )

                # Convert headers to dict
                response_headers = dict(response.headers)

                if not response.is_success:
                    return {
                        "success": False,
                        "status": response.status_code,
                        "headers": response_headers,
                        "error": f"HTTP error! status: {response.status_code}",
                    }

                try:
                    data = response.json()
                except json.JSONDecodeError:
                    data = response.text

                return {
                    "success": True,
                    "data": data,
                    "status": response.status_code,
                    "headers": response_headers,
                }

        except Exception:
            logger.exception("Request failed")
            raise

    async def request(self, endpoint: str, options: RequestOptions | None = None) -> ApiResponse:
        """Make HTTP request with retry functionality.

        Args:
            endpoint: API endpoint
            options: Request options

        Returns:
            API response
        """
        # [AI GENERATED] Main request method with retry logic for various status codes
        if options is None:
            options = {}

        merged_retry_config = {**self.retry_config}
        if "retry_config" in options:
            merged_retry_config.update(options["retry_config"])

        last_error: Exception | None = None
        current_endpoint = endpoint

        for attempt in range(merged_retry_config["max_retries"] + 1):
            try:
                response = await self._perform_request(current_endpoint, options)

                # Handle 202 Accepted
                if response.get("status") == HTTP_ACCEPTED and merged_retry_config["enable_retry_for_202"]:
                    # Return result if this is the last attempt
                    if attempt >= merged_retry_config["max_retries"]:
                        return response

                    headers = response.get("headers", {})
                    sp_resource_path = headers.get("sp-resource-path")
                    retry_after = headers.get("retry-after")

                    if retry_after:
                        delay = self._parse_retry_after(retry_after)
                        await asyncio.sleep(delay)

                    # Use new endpoint if sp-resource-path is provided
                    if sp_resource_path:
                        current_endpoint = sp_resource_path
                        options = {**options, "method": HttpMethod.GET, "body": None}

                    continue

                # Return success response
                if response.get("success"):
                    return response

                # Check if should retry
                status = response.get("status")
                if not self._should_retry(status, attempt):
                    return response

                # Handle 429 Too Many Requests
                if status == HTTP_TOO_MANY_REQUESTS and merged_retry_config["enable_retry_for_429"]:
                    # Return result if this is the last attempt
                    if attempt >= merged_retry_config["max_retries"]:
                        return response

                    headers = response.get("headers", {})
                    retry_after = headers.get("retry-after")
                    delay = self._parse_retry_after(retry_after)
                    await asyncio.sleep(delay)
                    continue

                # Return other errors
                return response

            except Exception as error:
                last_error = error

                # Raise error if this is the last attempt
                if attempt == merged_retry_config["max_retries"]:
                    raise last_error from None

                # Wait before retry for network errors
                await asyncio.sleep(min(1.0 * (2**attempt), 5.0))

        # Should not reach here, but raise error for safety
        if last_error:
            raise last_error
        msg = "Request failed after all retries"
        raise RuntimeError(msg)

    async def get(self, endpoint: str, headers: dict[str, str] | None = None) -> ApiResponse:
        """Make GET request.

        Args:
            endpoint: API endpoint
            headers: Request headers

        Returns:
            API response
        """
        # [AI GENERATED] GET request wrapper
        return await self.request(endpoint, {"method": HttpMethod.GET, "headers": headers})

    async def post(
        self, endpoint: str, data: JsonValue | None = None, headers: dict[str, str] | None = None
    ) -> ApiResponse:
        """Make POST request with JSON data.

        Args:
            endpoint: API endpoint
            data: Request data
            headers: Request headers

        Returns:
            API response
        """
        # [AI GENERATED] POST request wrapper with JSON serialization
        request_headers = {"Content-Type": "application/json"}
        if headers:
            request_headers.update(headers)

        body = json.dumps(data) if data is not None else None

        return await self.request(endpoint, {"method": HttpMethod.POST, "body": body, "headers": request_headers})

    async def post_text(self, endpoint: str, text: str, headers: dict[str, str] | None = None) -> ApiResponse:
        """Make POST request with text data.

        Args:
            endpoint: API endpoint
            text: Text data
            headers: Request headers

        Returns:
            API response
        """
        # [AI GENERATED] POST request wrapper for text/plain content
        request_headers = {"Content-Type": "text/plain"}
        if headers:
            request_headers.update(headers)

        return await self.request(endpoint, {"method": HttpMethod.POST, "body": text, "headers": request_headers})

    async def post_form(
        self, endpoint: str, form_data: dict[str, Any], headers: dict[str, str] | None = None
    ) -> ApiResponse:
        """Make POST request with form data.

        Args:
            endpoint: API endpoint
            form_data: Form data
            headers: Request headers

        Returns:
            API response
        """
        # [AI GENERATED] POST request wrapper for multipart/form-data
        # Note: This is a simplified implementation
        # In a real implementation, you'd need to handle multipart encoding properly
        request_headers = {}
        if headers:
            # Exclude Content-Type as httpx will set it automatically for multipart
            request_headers = {k: v for k, v in headers.items() if k.lower() != "content-type"}

        try:
            async with httpx.AsyncClient(timeout=self.config["timeout"]) as client:
                response = await client.post(
                    f"{self.config['base_url']}{endpoint}",
                    headers={"Authorization": f"Bearer {self.config['api_key']}", **request_headers},
                    files=form_data,
                )

                response_headers = dict(response.headers)

                if not response.is_success:
                    return {
                        "success": False,
                        "status": response.status_code,
                        "headers": response_headers,
                        "error": f"HTTP error! status: {response.status_code}",
                    }

                try:
                    data = response.json()
                except json.JSONDecodeError:
                    data = response.text

                return {
                    "success": True,
                    "data": data,
                    "status": response.status_code,
                    "headers": response_headers,
                }

        except Exception:
            logger.exception("Form request failed")
            raise

    async def put(
        self, endpoint: str, data: JsonValue | None = None, headers: dict[str, str] | None = None
    ) -> ApiResponse:
        """Make PUT request.

        Args:
            endpoint: API endpoint
            data: Request data
            headers: Request headers

        Returns:
            API response
        """
        # [AI GENERATED] PUT request wrapper
        body = json.dumps(data) if data is not None else None

        return await self.request(endpoint, {"method": HttpMethod.PUT, "body": body, "headers": headers})

    async def delete(self, endpoint: str, headers: dict[str, str] | None = None) -> ApiResponse:
        """Make DELETE request.

        Args:
            endpoint: API endpoint
            headers: Request headers

        Returns:
            API response
        """
        # [AI GENERATED] DELETE request wrapper
        return await self.request(endpoint, {"method": HttpMethod.DELETE, "headers": headers})

    async def request_without_auth(self, endpoint: str, options: RequestOptions | None = None) -> ApiResponse:
        """Make request without authentication.

        Args:
            endpoint: API endpoint
            options: Request options

        Returns:
            API response
        """
        # [AI GENERATED] Request method without authentication header
        if options is None:
            options = {}

        url = f"{self.config['base_url']}{endpoint}"
        method = options.get("method", HttpMethod.GET)
        headers = {"Content-Type": "application/json"}

        if "headers" in options:
            headers.update(options["headers"])

        timeout = options.get("timeout", self.config["timeout"])

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.request(
                    method=method.value,
                    url=url,
                    headers=headers,
                    content=options.get("body"),
                )

                if not response.is_success:
                    error_response: ErrorResponse = {
                        "error": f"HTTP error! status: {response.status_code}",
                        "status": response.status_code,
                        "message": None,
                    }
                    raise ApiError(response.status_code, error_response)

                try:
                    data = response.json()
                except json.JSONDecodeError:
                    data = response.text

                return {
                    "success": True,
                    "data": data,
                    "status": response.status_code,
                }

        except ApiError:
            raise
        except Exception:
            logger.exception("Request without auth failed")
            raise

    async def request_with_csrf(
        self, endpoint: str, session_cookie: str, csrf_token: str, options: RequestOptions | None = None
    ) -> ApiResponse:
        """Make request with CSRF token.

        Args:
            endpoint: API endpoint
            session_cookie: Session cookie
            csrf_token: CSRF token
            options: Request options

        Returns:
            API response
        """
        # [AI GENERATED] Request method with CSRF token and session cookie
        if options is None:
            options = {}

        url = f"{self.config['base_url']}{endpoint}"
        method = options.get("method", HttpMethod.POST)
        headers = {
            "Cookie": f"{session_cookie}; csrf={csrf_token}",
            "X-CSRF-Token": csrf_token,
            "Content-Type": "application/json",
        }

        if "headers" in options:
            headers.update(options["headers"])

        timeout = options.get("timeout", self.config["timeout"])

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.request(
                    method=method.value,
                    url=url,
                    headers=headers,
                    content=options.get("body"),
                )

                if not response.is_success:
                    error_response: ErrorResponse = {
                        "error": f"HTTP error! status: {response.status_code}",
                        "status": response.status_code,
                        "message": None,
                    }
                    raise ApiError(response.status_code, error_response)

                try:
                    data = response.json()
                except json.JSONDecodeError:
                    data = response.text

                return {
                    "success": True,
                    "data": data,
                    "status": response.status_code,
                }

        except ApiError:
            raise
        except Exception:
            logger.exception("CSRF request failed")
            raise
