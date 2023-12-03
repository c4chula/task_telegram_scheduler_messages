from loguru import logger
from pyrogram.client import Client
from pyrogram.types import Message

from tg_assistant.users.service import UserService


async def get_newbies_for_today(_: Client, msg: Message) -> None:
    logger.debug(f'get_newbies handler started via "{msg.text}"')
    users = [
        f"{user.user_telegram_id:<20}|{user.created_at.strftime('%H:%M:%S'):^30}"
        for user in await UserService().get_newbies_for_today()
    ]
    text = "\n".join(users) + f"\nTotal For Today {len(users)}"
    await msg.reply(text)


async def echo(_: Client, msg: Message) -> None:
    await msg.reply(msg.text)
