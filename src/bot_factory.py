from aiogram import Bot, Dispatcher

from .configs.schemas import BotConfig


async def start_bot(bot_config: BotConfig) -> None:
    """Function for configure and start telegram bot"""
    dp = Dispatcher()

    bot = Bot(bot_config.token)
    await dp.start_polling(bot)
