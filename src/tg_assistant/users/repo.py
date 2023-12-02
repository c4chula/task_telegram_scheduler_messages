from collections.abc import Sequence
from typing import Any

from sqlalchemy import delete, insert, select

from tg_assistant.database import AsyncSessionFactory

from .models import User
from .schema import UserCreate


class UserRepo(AsyncSessionFactory):
    def __init__(self, *args: Any, **kwargs: dict[str, Any]):
        super().__init__(*args, **kwargs)

    async def get_users(self) -> Sequence[User]:
        stmt = select(User)

        session = await super().get_session()
        return (await session.execute(stmt)).scalars().fetchall()

    async def get_user(self, id: int) -> User | None:
        stmt = select(User).where(User.id == id)

        session = await super().get_session()
        return (await session.execute(stmt)).scalar_one_or_none()

    async def create_user(self, data: UserCreate) -> User | None:
        stmt = (
            insert(User)
            .values(user_telelegram_id=data.user_telegram_id)
            .returning(User)
        )

        session = await super().get_session()
        user = (await session.execute(stmt)).scalar_one_or_none()
        await session.commit()
        return user

    async def delete_user(self, id: int) -> None:
        stmt = delete(User).where(User.id == id)

        session = await super().get_session()
        await session.execute(stmt)
        await session.commit()