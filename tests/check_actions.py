import logging
import os

from dotenv import load_dotenv
from loguru import logger

from simplise_api_client import (
    SimpliseClient,
    action_and,
    action_bool,
    action_decimal_add,
    action_decimal_mul,
    action_input,
    action_obj,
)

logging.basicConfig(level=logging.INFO)

load_dotenv()
client = SimpliseClient(api_key=os.getenv("SIMPLISE_TEST_BEARER_TOKEN", "default_token"))


def check_decimal_operations() -> None:
    """Check decimal operations."""
    # 小数点の加算、乗算、減算、除算の操作をテスト
    logger.info("Testing decimal operations...")

    logger.info(
        "ライブラリを使用した実行: {}",
        client.action.execute(
            action_decimal_add(10, action_input("value"), action_decimal_mul(3, 4)), action_obj("value", "5")
        ),
    )
    logger.info(
        "JsonLogicを使用した実行: {}",
        client.action.execute_logic(
            {"decimal.add": ["10", {"input": ["value"]}, {"decimal.mul": ["3", "4"]}]}, {"value": "5"}
        ),
    )


def check_bool_operations() -> None:
    """Check boolean operations."""
    # ブール値の操作をテスト
    logger.info("Testing boolean operations...")

    logger.info(
        "ライブラリを使用した実行: {}",
        client.action.execute(
            action_bool("True")  # trueが返される
        ),
    )
    logger.info(
        "JsonLogicを使用した実行: {}",
        client.action.execute_logic(
            {"bool": 0}  # 0はfalseとして扱われる
        ),
    )


def check_logic_operations() -> None:
    """Check logic operations."""
    # 論理演算のテスト
    logger.info("Testing logic operations...")

    logger.info(
        "ライブラリを使用した実行: {}",
        client.action.execute(
            action_and(action_bool("True"), action_bool("True")),
        ),
    )
    logger.info(
        "JsonLogicを使用した実行: {}", client.action.execute_logic({"and": [{"bool": ["0"]}, {"bool": ["True"]}]})
    )


if __name__ == "__main__":
    try:
        # check_decimal_operations()
        check_bool_operations()
        check_logic_operations()
    except Exception:
        logger.exception("Error occurred")
