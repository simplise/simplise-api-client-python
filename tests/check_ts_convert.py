import asyncio
import logging
import os
from typing import Any

from dotenv import load_dotenv

from simplise_client import SimpliseClient

# [AI GENERATED] Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main() -> None:
    """Main function to test the Simplise API client."""
    # [AI GENERATED] Load environment variables and create client
    load_dotenv()
    client = SimpliseClient(api_key=os.getenv("SIMPLISE_TEST_BEARER_TOKEN", "default_token"))

    try:
        # [AI GENERATED] Execute decimal add operation with await
        # Using JsonLogic directly since the Action.decimal.add typing seems complex
        action_rule = {"decimal.add": ["10", {"input": ["value"]}, {"decimal.mul": ["3", "4"]}]}
        input_data: dict[str, Any] = {"value": "5"}

        result = await client.action.execute_logic(action_rule, input_data)
        logger.info("Decimal add result: %s", result)
    except Exception:
        logger.exception("Error executing action")


if __name__ == "__main__":
    asyncio.run(main())
