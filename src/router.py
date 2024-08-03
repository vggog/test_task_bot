from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from .buttons import main_buttons
from .state import AddMessageState


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
async def all_messages_route(callback: CallbackQuery) -> None:
    """
    Route for get all messages.
    """
    await callback.answer()
    await callback.message.delete_reply_markup()

    await callback.message.answer("Ваши сообщения:")
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
async def add_message_router(message: Message, state: FSMContext) -> None:
    """Route for send message to server"""
    await message.answer("Ваше сообщение отправлено")
    await message.answer(
        "Что пожелаете сотворить?",
        reply_markup=main_buttons(),
    )
    await state.clear()
