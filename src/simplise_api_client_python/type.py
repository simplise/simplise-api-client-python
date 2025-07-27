from typing import TYPE_CHECKING, Any, TypedDict

if TYPE_CHECKING:
    from simplise_api_client_python.action import Operation

# Operation types
type OperationArg = Operation | str | int

# JsonLogic rule types
type JsonLogicValue = str | int | float | bool | None | dict[str, Any] | list[Any]
type JsonLogicRule = dict[str, JsonLogicValue]


class ExecuteLogic(TypedDict):
    """TypedDict for execute_logic method parameters."""

    rule: JsonLogicRule
    data: dict[str, Any] | None
