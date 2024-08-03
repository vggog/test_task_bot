import os

from .schemas import BotConfig


def load_bot_config():
    """Create configs for bot"""
    bot_token = os.getenv("BOT_TOKEN")

    if bot_token is None:
        raise NameError("Secret BOT_TOKEN not found.")

    return BotConfig(
        token=bot_token
    )
