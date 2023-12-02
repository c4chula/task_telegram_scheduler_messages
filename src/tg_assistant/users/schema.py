from datetime import datetime

from tg_assistant.schema import BaseSchema


class UserCreate(BaseSchema):
    user_telegram_id: str


class UserResponse(UserCreate):
    id: int
    created_at: datetime
