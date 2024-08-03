from aiogram.fsm.state import State, StatesGroup


class AddMessageState(StatesGroup):
    message = State()
