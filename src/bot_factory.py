from aiogram import Bot, Dispatcher

from .configs.schemas import BotConfig
from .router import router


async def start_bot(bot_config: BotConfig) -> None:
    """Function for configure and start telegram bot"""
    dp = Dispatcher()
    dp.include_router(router)

    bot = Bot(bot_config.token)
    await dp.start_polling(bot)
