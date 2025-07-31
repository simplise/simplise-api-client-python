"""This module provides logical AND operation."""

import logging

from simplise_api_client.actions import action_bool
from simplise_api_client.actions.utils import Operation
from simplise_api_client.type import OperationArg

logger = logging.getLogger(__name__)


def action_and(*conditions: OperationArg) -> Operation:
    """Execute logical AND operation on multiple conditions.

    Evaluates multiple logical values from left to right and returns true
    if all conditions are truthy.

    Args:
        *conditions (OperationArg): Conditions to evaluate.

    Returns:
        Operation: An operation representing the logical AND of the conditions.
    """
    # [AI GENERATED] 論理積演算を実行し、すべての条件がtrueの場合のみtrueを返す
    logger.debug("Executing logical AND operation with %s conditions", len(conditions))

    processed_conditions = []
    for condition in conditions:
        # もしconditionがbool値の場合、action_bool変換する
        processed_condition = action_bool(condition) if type(condition) is bool else condition
        processed_conditions.append(processed_condition)

    return Operation("and", *processed_conditions)
