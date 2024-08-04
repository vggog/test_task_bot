import aiohttp

from .exceptions import RequestError


class Service:

    @staticmethod
    async def get_all_messages() -> list[dict]:
        """Method for get all messages"""
        async with aiohttp.ClientSession() as client:
            response = await client.get("http://server:8000/api/v1/messages")
            if response.status != 200:
                raise RequestError("Ошибка получения сообщений")
            return await response.json()

    @staticmethod
    async def send_message(user_id: str, username: str, text: str) -> None:
        """Method for send message to server"""
        async with aiohttp.ClientSession() as client:
            response = await client.post(
                url="http://server:8000/api/v1/message",
                json={
                    "user_id": user_id,
                    "username": username,
                    "text": text,
                },
            )

            if response.status != 201:
                raise RequestError("Ошибка создания сообщения")
