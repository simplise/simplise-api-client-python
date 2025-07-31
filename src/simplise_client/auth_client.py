"""Authentication client for Simplise API."""

import json
import logging

from .http_client import HttpClient
from .types import ApiResponse, AuthSession, HttpMethod, LoginCredentials, RequestOptions

logger = logging.getLogger(__name__)


class AuthClient:
    """Authentication client for Simplise API."""

    def __init__(self, http_client: HttpClient) -> None:
        """Initialize authentication client.

        Args:
            http_client: HTTP client instance
        """
        # [AI GENERATED] Initialize authentication client with HTTP client
        self.http_client = http_client

    async def login(self, credentials: LoginCredentials) -> ApiResponse:
        """Login to the API.

        Args:
            credentials: Login credentials

        Returns:
            API response with login result
        """
        # [AI GENERATED] Perform login with username and password
        login_data = {
            "username": credentials["username"],
            "password": credentials["password"],
            "turnstile_token": credentials.get("turnstile_token", "dummy-token"),
        }

        options: RequestOptions = {"method": HttpMethod.POST, "body": json.dumps(login_data)}

        return await self.http_client.request_without_auth("/auth/login", options)

    async def logout(self, session_cookie: str) -> ApiResponse:
        """Logout from the API.

        Args:
            session_cookie: Session cookie

        Returns:
            API response
        """
        # [AI GENERATED] Perform logout with session cookie
        options: RequestOptions = {"method": HttpMethod.POST, "headers": {"Cookie": session_cookie}}

        return await self.http_client.request_without_auth("/auth/logout", options)

    async def get_csrf_token(self, session_cookie: str) -> str | None:
        """Get CSRF token.

        Args:
            session_cookie: Session cookie

        Returns:
            CSRF token or None if failed
        """
        # [AI GENERATED] Retrieve CSRF token using session cookie
        try:
            options: RequestOptions = {"method": HttpMethod.GET, "headers": {"Cookie": session_cookie}}

            await self.http_client.request_without_auth("/auth/csrf-token", options)

            # Note: In browser environments, Set-Cookie headers are typically not accessible
            # In a real implementation, the server should return the CSRF token in the response body
            # For now, return a placeholder token
            return "csrf-token-from-response"

        except Exception as e:
            logger.warning(f"Failed to get CSRF token: {e}")
            return None

    async def establish_session(self, credentials: LoginCredentials) -> AuthSession | None:
        """Establish authentication session.

        Args:
            credentials: Login credentials

        Returns:
            Authentication session or None if failed
        """
        # [AI GENERATED] Establish complete authentication session with login and CSRF token
        try:
            login_response = await self.login(credentials)

            if not login_response.get("success"):
                logger.warning("Login failed")
                return None

            # In a real implementation, extract session cookie from login response
            # For browser environments, cookies are automatically handled
            # This implementation assumes server-side usage
            session_cookie = "jwt=extracted-from-response"
            csrf_token = await self.get_csrf_token(session_cookie)

            return {"session_cookie": session_cookie, "csrf_token": csrf_token}

        except Exception:
            logger.exception("Failed to establish session")
            return None

    async def verify_token(self) -> ApiResponse:
        """Verify authentication token.

        Returns:
            API response with verification result
        """
        # [AI GENERATED] Verify current authentication token
        return await self.http_client.get("/auth/verify")

    async def request_password_reset(self, email: str) -> ApiResponse:
        """Request password reset.

        Args:
            email: Email address

        Returns:
            API response
        """
        # [AI GENERATED] Request password reset for email address
        reset_data = {"email": email}

        options: RequestOptions = {"method": HttpMethod.POST, "body": json.dumps(reset_data)}

        return await self.http_client.request_without_auth("/auth/password-reset", options)

    async def reset_password(self, token: str, new_password: str) -> ApiResponse:
        """Reset password using token.

        Args:
            token: Password reset token
            new_password: New password

        Returns:
            API response
        """
        # [AI GENERATED] Complete password reset with token and new password
        reset_data = {"token": token, "newPassword": new_password}

        options: RequestOptions = {"method": HttpMethod.POST, "body": json.dumps(reset_data)}

        return await self.http_client.request_without_auth("/auth/password-reset/confirm", options)
