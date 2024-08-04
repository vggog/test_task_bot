from .service import Service
from .configs import load_bot_settings


def build_service() -> Service:
    """Function for build Service class"""
    return Service(bot_settings=load_bot_settings())
