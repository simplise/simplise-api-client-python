"""# input

get parameters for actions.
You can get the HTTP request body content when executed with a POST request.

Documents: https://api.usebootstrap.org/spec/doc/action/data/input.md
"""
# アクションに対するパラメータを取得します
# POSTリクエストで実行した際のHTTPリクエストボディコンテンツを取得できます。

import logging

from simplise_api_client.actions.utils import Operation

logger = logging.getLogger(__name__)


def action_input(key: str) -> Operation:
    """Create an input reference.

    Args:
        key (str): The input key to reference

    Returns:
        Operation: An operation that references the input key
    """
    logger.debug(f"Creating input reference for key: {key}")
    return Operation("input", key)


def action_obj(key: str, value: str) -> dict[str, str]:
    """Create an object with a key-value pair.

    Args:
        key (str): The key for the object
        value (str): The value for the object

    Returns:
        Operation: An operation that creates an object with the specified key and value
    """
    logger.debug(f"Creating object with key: {key}, value: {value}")
    return {key: value}
