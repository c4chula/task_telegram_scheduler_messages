from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from tg_assistant.config import cfg

engine = create_async_engine(cfg.sqlite_url)
sessionmaker = async_sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False,
)


class Base(DeclarativeBase):
    ...


class AsyncSessionFactory:
    async def get_session(self) -> AsyncSession:
        async with sessionmaker() as session:
            return session
