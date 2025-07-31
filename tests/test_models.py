"""Pydanticモデルのテスト。

このモジュールには、API データ検証のためのPydanticモデルの
包括的なテストケースが含まれています。
"""

from typing import TYPE_CHECKING, Any

import pytest
from pydantic import ValidationError

from simplise_api_client.models import (
    ActionExecuteRequest,
    ActionExecuteResponse,
    ActionLogicRequest,
    ActionLogicResponse,
    JsonLogicExecuteRequest,
    JsonLogicExecuteResponse,
)

if TYPE_CHECKING:
    from simplise_api_client.type import JsonLogicRule


class TestActionLogicRequest:
    """ActionLogicRequestモデルのテストケース。

    action-logicエンドポイントへのリクエストデータ検証をテストします。
    """

    def test_valid_request_with_rule_only(self) -> None:
        """ルールのみを含む有効なリクエストをテスト。

        input_dataなしで有効なJsonLogicルールを含むリクエストを検証します。
        """
        # [AI GENERATED] 有効なJsonLogicルールを定義
        rule: JsonLogicRule = {"and": [{"==": [{"var": "age"}, 30]}, {"==": [{"var": "name"}, "John"]}]}

        # [AI GENERATED] モデルを作成
        request = ActionLogicRequest(rule=rule, input_data=None)

        # [AI GENERATED] データが正しく設定されることを検証
        assert request.rule == rule
        assert request.input_data is None

    def test_valid_request_with_rule_and_input_data(self) -> None:
        """ルールと入力データを含む有効なリクエストをテスト。

        JsonLogicルールと入力データの両方を含むリクエストを検証します。
        """
        # [AI GENERATED] 有効なJsonLogicルールと入力データを定義
        rule: JsonLogicRule = {"==": [{"var": "age"}, 30]}
        input_data = {"age": 30, "name": "John"}

        # [AI GENERATED] モデルを作成
        request = ActionLogicRequest(rule=rule, input_data=input_data)

        # [AI GENERATED] データが正しく設定されることを検証
        assert request.rule == rule
        assert request.input_data == input_data

    def test_invalid_request_missing_rule(self) -> None:
        """必須フィールドが欠けている無効なリクエストをテスト。

        ruleフィールドが提供されていない場合のバリデーションエラーを検証します。
        """
        # [AI GENERATED] ruleなしでモデル作成を試行し、ValidationErrorが発生することを検証
        with pytest.raises(ValidationError) as exc_info:
            ActionLogicRequest()  # type: ignore[call-arg]

        # [AI GENERATED] エラーメッセージにruleフィールドが含まれることを検証
        assert "rule" in str(exc_info.value)


class TestActionLogicResponse:
    """ActionLogicResponseモデルのテストケース。

    action-logicエンドポイントからのレスポンスデータ検証をテストします。
    """

    def test_valid_response(self) -> None:
        """有効なレスポンスをテスト。

        結果文字列を含む有効なレスポンスを検証します。
        """
        # [AI GENERATED] 有効な結果文字列を定義
        result = "Operation completed successfully"

        # [AI GENERATED] モデルを作成
        response = ActionLogicResponse(result=result)

        # [AI GENERATED] データが正しく設定されることを検証
        assert response.result == result

    def test_invalid_response_missing_result(self) -> None:
        """必須フィールドが欠けている無効なレスポンスをテスト。

        resultフィールドが提供されていない場合のバリデーションエラーを検証します。
        """
        # [AI GENERATED] resultなしでモデル作成を試行し、ValidationErrorが発生することを検証
        with pytest.raises(ValidationError) as exc_info:
            ActionLogicResponse()  # type: ignore[call-arg]

        # [AI GENERATED] エラーメッセージにresultフィールドが含まれることを検証
        assert "result" in str(exc_info.value)


class TestActionExecuteRequest:
    """ActionExecuteRequestモデルのテストケース。

    アクション実行のリクエストデータ検証をテストします。
    """

    def test_valid_request(self) -> None:
        """有効なリクエストをテスト。

        操作データと入力データを含む有効なリクエストを検証します。
        """
        # [AI GENERATED] 有効な操作データと入力データを定義
        operation_data: dict[str, Any] = {"add": [1, 2]}
        input_data = {"value1": "1", "value2": "2"}

        # [AI GENERATED] モデルを作成
        request = ActionExecuteRequest(operation_data=operation_data, input_data=input_data)

        # [AI GENERATED] データが正しく設定されることを検証
        assert request.operation_data == operation_data
        assert request.input_data == input_data

    def test_invalid_request_missing_fields(self) -> None:
        """必須フィールドが欠けている無効なリクエストをテスト。

        必須フィールドが提供されていない場合のバリデーションエラーを検証します。
        """
        # [AI GENERATED] 必須フィールドなしでモデル作成を試行し、ValidationErrorが発生することを検証
        with pytest.raises(ValidationError) as exc_info:
            ActionExecuteRequest()  # type: ignore[call-arg]

        # [AI GENERATED] エラーメッセージに必須フィールドが含まれることを検証
        error_message = str(exc_info.value)
        assert "operation_data" in error_message
        assert "input_data" in error_message


class TestActionExecuteResponse:
    """ActionExecuteResponseモデルのテストケース。

    アクション実行のレスポンスデータ検証をテストします。
    """

    def test_valid_response(self) -> None:
        """有効なレスポンスをテスト。

        結果文字列を含む有効なレスポンスを検証します。
        """
        # [AI GENERATED] 有効な結果文字列を定義
        result = "3"

        # [AI GENERATED] モデルを作成
        response = ActionExecuteResponse(result=result)

        # [AI GENERATED] データが正しく設定されることを検証
        assert response.result == result


class TestJsonLogicExecuteRequest:
    """JsonLogicExecuteRequestモデルのテストケース。

    JsonLogicルール実行のリクエストデータ検証をテストします。
    """

    def test_valid_request_with_rule_only(self) -> None:
        """ルールのみを含む有効なリクエストをテスト。

        dataなしで有効なJsonLogicルールを含むリクエストを検証します。
        """
        # [AI GENERATED] 有効なJsonLogicルールを定義
        rule: JsonLogicRule = {"==": [{"var": "x"}, 10]}

        # [AI GENERATED] モデルを作成
        request = JsonLogicExecuteRequest(rule=rule, data=None)

        # [AI GENERATED] データが正しく設定されることを検証
        assert request.rule == rule
        assert request.data is None

    def test_valid_request_with_rule_and_data(self) -> None:
        """ルールとデータを含む有効なリクエストをテスト。

        JsonLogicルールとデータの両方を含むリクエストを検証します。
        """
        # [AI GENERATED] 有効なJsonLogicルールとデータを定義
        rule: JsonLogicRule = {"==": [{"var": "x"}, 10]}
        data: dict[str, Any] = {"x": 10, "y": "test"}

        # [AI GENERATED] モデルを作成
        request = JsonLogicExecuteRequest(rule=rule, data=data)

        # [AI GENERATED] データが正しく設定されることを検証
        assert request.rule == rule
        assert request.data == data


class TestJsonLogicExecuteResponse:
    """JsonLogicExecuteResponseモデルのテストケース。

    JsonLogicルール実行のレスポンスデータ検証をテストします。
    """

    def test_valid_response(self) -> None:
        """有効なレスポンスをテスト。

        結果文字列を含む有効なレスポンスを検証します。
        """
        # [AI GENERATED] 有効な結果文字列を定義
        result = "true"

        # [AI GENERATED] モデルを作成
        response = JsonLogicExecuteResponse(result=result)

        # [AI GENERATED] データが正しく設定されることを検証
        assert response.result == result

    def test_invalid_response_missing_result(self) -> None:
        """必須フィールドが欠けている無効なレスポンスをテスト。

        resultフィールドが提供されていない場合のバリデーションエラーを検証します。
        """
        # [AI GENERATED] resultなしでモデル作成を試行し、ValidationErrorが発生することを検証
        with pytest.raises(ValidationError) as exc_info:
            JsonLogicExecuteResponse()  # type: ignore[call-arg]

        # [AI GENERATED] エラーメッセージにresultフィールドが含まれることを検証
        assert "result" in str(exc_info.value)
