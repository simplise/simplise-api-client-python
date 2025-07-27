import os

from dotenv import load_dotenv
from loguru import logger

from simplise_api_client_python import SimpliseClient, action

load_dotenv()
client = SimpliseClient(api_key=os.getenv("SIMPLISE_TEST_BEARER_TOKEN", "default_token"))

# ライブラリ モデルを利用した実行
try:
    result = client.action.execute(action.decimal.add(10, action.input_ref("value")), action.decimal.mul(3, 4))
    logger.info(f"Execution result: {result}")
except Exception as e:
    logger.error(f"Error occurred: {e}")

# JsonLogic Rule実行
try:
    result = client.action.execute_logic(
        {"decimal.add": ["10", {"input": ["value"]}, {"decimal.mul": ["3", "4"]}]}, {"value": "5"}
    )
    logger.info(f"Execution result: {result}")
except Exception as e:
    logger.error(f"Error occurred: {e}")
