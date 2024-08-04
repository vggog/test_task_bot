from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from .configs.schemas import BotConfig
from .router import router
from .builder import build_service


async def start_bot(bot_config: BotConfig) -> None:
    """Function for configure and start telegram bot"""
    dp = Dispatcher(
        service=build_service(),
    )
    dp.include_router(router)

    bot = Bot(
        bot_config.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)
