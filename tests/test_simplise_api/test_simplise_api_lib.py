import os

from dotenv import load_dotenv
from loguru import logger

from simplise_api_client import (
    SimpliseClient,
    action_decimal_add,
    action_decimal_mul,
    action_input,
    action_obj,
)

load_dotenv()
client = SimpliseClient(api_key=os.getenv("SIMPLISE_TEST_BEARER_TOKEN", "default_token"))

# ライブラリ モデルを利用した実行
try:
    result = client.action.execute(
        action_decimal_add(10, action_input("value"), action_decimal_mul(3, 4)), data=action_obj("value", "5")
    )
    logger.info(f"Execution result: {result}")
except Exception as e:
    logger.exception(f"Error occurred: {e}")

# JsonLogic Rule実行
try:
    result = client.action.execute_logic(
        {"decimal.add": ["10", {"input": ["value"]}, {"decimal.mul": ["3", "4"]}]}, {"value": "5"}
    )
    logger.info(f"Execution result: {result}")

    # result = client.action.execute_logic({"gsun": ["10"]})
    # logger.info(f"Execution result: {result}")
except Exception as e:
    logger.exception(f"Error occurred: {e}")
