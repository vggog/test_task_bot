from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str


@dataclass
class BotSettings:
    server_url: str
