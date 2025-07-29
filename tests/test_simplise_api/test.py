import json
import os

import requests
from dotenv import load_dotenv
from loguru import logger

load_dotenv()


def call_action_logic_api():
    url = "https://api.usebootstrap.org/action-logic"

    # APIキーを環境変数から取得
    api_key = os.getenv("SIMPLISE_TEST_BEARER_TOKEN", "384443F6CC5980ED5EE623FD2A624157")

    headers = {"Authorization": f"Bearer {api_key}"}

    # アクションのJSONデータ
    action_data = {"decimal.add": ["10", {"input": ["value"]}, {"decimal.mul": ["3", "4"]}]}

    # 入力のJSONデータ
    input_data = {"value": "5"}

    # multipart/form-dataとしてデータを準備
    files = {
        "action": (None, json.dumps(action_data), "application/json"),
        "input": (None, json.dumps(input_data), "application/json"),
    }

    try:
        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()  # HTTPエラーをチェック

        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response: {response.text}")

        return response.json() if response.content else None

    except requests.exceptions.RequestException as e:
        logger.exception(f"API request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        logger.exception(f"Failed to parse JSON response: {e}")
        return None


if __name__ == "__main__":
    result = call_action_logic_api()
    if result:
        logger.info(f"API result: {result}")
