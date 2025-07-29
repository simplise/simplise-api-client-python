from typing import TYPE_CHECKING, Any, TypedDict

if TYPE_CHECKING:
    from simplise_api_client.actions import Operation

# Operation types
type OperationArg = Operation | str | int

# JsonLogic rule types
type JsonLogicValueSafetyStr = str | dict[str, str] | list[str]
type JsonLogicValue = JsonLogicValueSafetyStr | int | float | bool | dict[str, Any] | list[Any]
type JsonLogicRuleSafetyStr = dict[str, JsonLogicValueSafetyStr]
type JsonLogicRule = dict[str, JsonLogicValue]


class ExecuteLogic(TypedDict):
    """TypedDict for execute_logic method parameters."""

    rule: JsonLogicRule
    data: dict[str, Any] | None
