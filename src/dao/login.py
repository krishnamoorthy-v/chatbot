from src.service.basic_crud import BaseCRUD
from src.model.users import User
from typing import Type, TypeVar, Generic, Optional, List


class UserCRUD(BaseCRUD[User]):
    def __init__(self):
        super().__init__(User)

    async def get_by_email(self, email: str) -> Optional[User]:
        return await self.model.find_one(User.email == email)