"""This module provides functions to create input references and objects"""
# このモジュールは、入力参照とオブジェクトを作成する関数を提供します

from simplise_api_client.actions import Operation


def action_input(key: str) -> Operation:
    """Create an input reference.

    Args:
        key (str): The input key to reference

    Returns:
        Operation: An operation that references the input key
    """
    return Operation("input", key)


def action_obj(key: str, value: str) -> dict[str, str]:
    """Create an object with a key-value pair.

    Args:
        key (str): The key for the object
        value (str): The value for the object

    Returns:
        Operation: An operation that creates an object with the specified key and value
    """
    return {key: value}
