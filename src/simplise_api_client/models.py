"""Pydantic models for API data validation.

This module defines Pydantic models for validating API request and response data.
"""
# [AI GENERATED] APIデータのバリデーション用Pydanticモデルを定義

from typing import Any

from pydantic import BaseModel, Field

from simplise_api_client.type import JsonLogicRule


class ActionLogicRequest(BaseModel):
    """Request model for action-logic endpoint.

    action-logicエンドポイントへのリクエストデータを検証するためのモデル
    """

    rule: JsonLogicRule = Field(..., description="JsonLogic rule to execute")
    input_data: dict[str, Any] | None = Field(None, description="Optional input data")

    class Config:
        """Pydantic configuration."""

        arbitrary_types_allowed = True


class ActionLogicResponse(BaseModel):
    """Response model for action-logic endpoint.

    action-logicエンドポイントからのレスポンスデータを検証するためのモデル
    """

    result: str = Field(..., description="Result from the API")


class ActionExecuteRequest(BaseModel):
    """Request model for action execution.

    アクション実行のリクエストデータを検証するためのモデル
    """

    operation_data: JsonLogicRule = Field(..., description="Operation data in JsonLogic format")
    input_data: dict[str, str] | None = Field(..., description="Input data for the operation")

    class Config:
        """Pydantic configuration."""

        arbitrary_types_allowed = True


class ActionExecuteResponse(BaseModel):
    """Response model for action execution.

    アクション実行のレスポンスデータを検証するためのモデル
    """

    result: str = Field(..., description="Result of the operation execution")


class JsonLogicExecuteRequest(BaseModel):
    """Request model for JsonLogic rule execution.

    JsonLogicルール実行のリクエストデータを検証するためのモデル
    """

    rule: JsonLogicRule = Field(..., description="JsonLogic rule to execute")
    data: dict[str, Any] | None = Field(None, description="Optional data for the rule")

    class Config:
        """Pydantic configuration."""

        arbitrary_types_allowed = True


class JsonLogicExecuteResponse(BaseModel):
    """Response model for JsonLogic rule execution.

    JsonLogicルール実行のレスポンスデータを検証するためのモデル
    """

    result: str = Field(..., description="Result of the rule execution")
