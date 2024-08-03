import asyncio

from src.bot_factory import start_bot
from src.configs import load_bot_config


if __name__ == "__main__":
    asyncio.run(start_bot(load_bot_config()))
