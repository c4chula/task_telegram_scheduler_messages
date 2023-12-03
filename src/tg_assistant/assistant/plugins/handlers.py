from loguru import logger
from pyrogram.client import Client
from pyrogram.types import Message

from tg_assistant.users.service import UserService
from tg_assistant.users.schema import UserCreate


async def get_newbies_for_today(_: Client, msg: Message) -> None:
    logger.debug(f'/get_newbies handler started via "{msg.text}"')
    users = [
        f"{user.user_telegram_id:<20}|{user.created_at.strftime('%H:%M:%S'):^30}"
        for user in await UserService().get_newbies_for_today()
    ]
    text = "\n".join(users) + f"\nTotal For Today {len(users)}"
    await msg.reply(text)


async def welcome_newbie(_: Client, msg: Message) -> None:
    logger.debug(f'/welcome_newbie handler started via "{msg.text}"')
    user = await UserService().get_user_by_telegram_id(str(msg.from_user.id))
    if user is not None:
        return

    user = await UserService().create_user(
        UserCreate(user_telegram_id=str(msg.from_user.id))
    )
    logger.info(f"new {user=} was created")
