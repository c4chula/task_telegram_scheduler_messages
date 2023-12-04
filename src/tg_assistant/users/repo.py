from collections.abc import Sequence
from typing import Any
from loguru import logger

from sqlalchemy import delete, insert, or_, select

from tg_assistant.database import AsyncSessionFactory

from .models import User
from .schema import UserCreate


class UserRepo(AsyncSessionFactory):
    def __init__(self, *args: Any, **kwargs: dict[str, Any]):
        super().__init__(*args, **kwargs)

    async def get_users(self, *_: Any, **filters: dict[str, Any]) -> Sequence[User]:
        stmt = select(User)

        filter_set = [
            getattr(User, attr) == value
            for attr, value in filters.items()
            if hasattr(User, attr)
        ]

        if filter_set:
            stmt = stmt.filter(or_(*filter_set))

        session = await super().get_session()
        data = (await session.execute(stmt)).scalars().fetchall()
        await session.close()
        return data

    async def get_user(self, id: int) -> User | None:
        stmt = select(User).where(User.id == id)

        session = await super().get_session()
        data = (await session.execute(stmt)).scalar_one_or_none()
        await session.close()
        return data

    async def get_user_by_telegram_id(self, user_telegram_id: str) -> User | None:
        stmt = select(User).where(User.user_telegram_id == user_telegram_id)

        session = await super().get_session()
        data = (await session.execute(stmt)).scalar_one_or_none()
        await session.close()
        return data

    async def create_user(self, data: UserCreate) -> User | None:
        stmt = (
            insert(User)
            .values(user_telelegram_id=data.user_telegram_id)
            .returning(User)
        )

        session = await super().get_session()
        try:
            user = (await session.execute(stmt)).scalar_one_or_none()
            await session.commit()
            return user
        except Exception as e:
            logger.exception(e)
        finally:
            await session.close()

    async def delete_user(self, id: int) -> None:
        stmt = delete(User).where(User.id == id)

        session = await super().get_session()
        await session.execute(stmt)
        await session.commit()
        await session.close()
