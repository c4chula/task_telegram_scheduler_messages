from collections.abc import Callable
from typing import Any

from loguru import logger
from pyrogram.client import Client
from pyrogram.filters import Filter


class Assistant(Client):
    client_name = "assistant"

    def __init__(
        self,
        api_id: int,
        api_hash: str,
        *args: Any,
        **kwargs: dict[str, Any],
    ) -> None:
        super().__init__(Assistant.client_name, api_id, api_hash, *args, **kwargs)

    async def start(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        logger.info("assistant client just started :)")
        await super().start(*args, **kwargs)

    async def stop(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        logger.info("assistant client just stopped :(")
        await super().stop(*args, **kwargs)

    def on_message(self, filters: Filter | None = None, group: int = 0) -> Callable:
        return super().on_message(filters, group)
