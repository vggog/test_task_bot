from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup


def main_buttons() -> InlineKeyboardMarkup:
    """
    Function for creating inline buttons for text getting after start command
    """
    all_messages = InlineKeyboardButton(
        text="Все сообщения",
        callback_data="all_messages",
    )
    add_message = InlineKeyboardButton(
        text="Добавить сообщение",
        callback_data="add_message",
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [all_messages],
            [add_message],
        ]
    )
