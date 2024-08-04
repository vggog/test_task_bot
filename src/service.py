import aiohttp

from .exceptions import RequestError
from .configs.schemas import BotSettings


class Service:

    def __init__(self, bot_settings: BotSettings):
        self.bot_settings = bot_settings

    async def get_all_messages(self) -> list[dict]:
        """Method for get all messages"""
        async with aiohttp.ClientSession() as client:
            response = await client.get(
                self.bot_settings.server_url + "/api/v1/messages"
            )
            if response.status != 200:
                raise RequestError("Ошибка получения сообщений")
            return await response.json()

    async def send_message(self, user_id: str, username: str, text: str) -> None:
        """Method for send message to server"""
        async with aiohttp.ClientSession() as client:
            response = await client.post(
                url=self.bot_settings.server_url + "/api/v1/message",
                json={
                    "user_id": user_id,
                    "username": username,
                    "text": text,
                },
            )

            if response.status != 201:
                raise RequestError("Ошибка создания сообщения")
