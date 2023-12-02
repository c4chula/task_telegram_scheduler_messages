import asyncio

from pyrogram.client import Client

from tg_assistant.config import cfg


async def main() -> None:
    app = Client(
        "my_account",
        api_id=cfg.api_id,
        api_hash=cfg.api_hash,
    )


if __name__ == "__main__":
    asyncio.run(main())
