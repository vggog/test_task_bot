from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from .buttons import main_buttons
from .state import AddMessageState
from .service import Service
from .exceptions import RequestError


router = Router()


@router.message(CommandStart())
async def start_command_router(message: Message) -> None:
    """
    Start command route
    Send welcome message with two buttons for get all messages and send message
    """
    await message.answer(
        "Приветствую, что хотите сделать?",
        reply_markup=main_buttons(),
    )


@router.callback_query(F.data == "all_messages")
async def all_messages_route(
        callback: CallbackQuery,
        service: Service
) -> None:
    """
    Route for get all messages.
    """
    await callback.answer()
    await callback.message.delete_reply_markup()

    try:
        messages = await service.get_all_messages()
    except RequestError as e:
        await callback.message.answer(str(e))
    else:
        await callback.message.answer("Ваши сообщения:")
        for message in messages:
            await callback.message.answer(
                f"<b>{message['username']}</b>:\n"
                f"{message['text']}\n"
            )

    await callback.message.answer(
        "Что пожелаете сотворить?",
        reply_markup=main_buttons(),
    )


@router.callback_query(F.data == "add_message")
async def get_message_route(
        callback: CallbackQuery,
        state: FSMContext
) -> None:
    """Route for requesting the message the user wants to send"""
    await callback.answer()
    await callback.message.delete_reply_markup()

    await state.set_state(AddMessageState.message)
    await callback.message.answer("Введите сообщение:")


@router.message(AddMessageState.message)
async def add_message_router(
        message: Message,
        state: FSMContext,
        service: Service
) -> None:
    """Route for send message to server"""
    try:
        await service.send_message(
            user_id=str(message.from_user.id),
            username=message.from_user.username,
            text=message.text
        )
    except RequestError as e:
        await message.answer(str(e))
    else:
        await message.answer("Ваше сообщение отправлено")

    await message.answer(
        "Что пожелаете сотворить?",
        reply_markup=main_buttons(),
    )
    await state.clear()
