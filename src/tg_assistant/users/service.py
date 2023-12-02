from collections.abc import Sequence
from typing import Any

from .repo import UserRepo
from .schema import UserCreate, UserResponse


class UserService(UserRepo):
    def __init__(self, *args: Any, **kwargs: dict[str, Any]):
        super().__init__(*args, **kwargs)

    async def get_users(self) -> Sequence[UserResponse]:
        users = await super().get_users()
        return [UserResponse.model_validate(data) for data in users]

    async def create_user(self, data: UserCreate) -> UserResponse | None:
        user = await super().create_user(data)
        if user is None:
            return None
        return UserResponse.model_validate(user)

    async def delete_user(self, id: int) -> None:
        await super().delete_user(id)
