import os

from .schemas import BotConfig, BotSettings


def load_bot_config():
    """Create configs for bot"""
    bot_token = os.getenv("BOT_TOKEN")

    if bot_token is None:
        raise NameError("Secret BOT_TOKEN not found.")

    return BotConfig(
        token=bot_token
    )


def load_bot_settings():
    """Create settings for bot"""
    server_url = os.getenv("SERVER_URL")

    if server_url is None:
        raise NameError("Secret SERVER_URL not found.")

    return BotSettings(
        server_url=server_url
    )
