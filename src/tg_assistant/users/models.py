from datetime import datetime

from sqlalchemy import Integer, String
from sqlalchemy.dialects.sqlite import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_telegram_id: Mapped[str] = mapped_column(String(512))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
