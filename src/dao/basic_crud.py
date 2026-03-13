from typing import Type, TypeVar, Generic, Optional, List
from beanie import Document
from bson import ObjectId

T = TypeVar("T", bound=Document)


class BaseCRUD(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def create(self, data: dict) -> T:
        obj = self.model(**data)
        await obj.insert()
        return obj

    async def get_by_id(self, id: str) -> Optional[T]:
        return await self.model.get(ObjectId(id))

    async def get_one(self, filter_query: dict) -> Optional[T]:
        return await self.model.find_one(filter_query)

    async def get_all(self) -> List[T]:
        return await self.model.find_all().to_list()

    async def update(self, id: str, update_data: dict) -> Optional[T]:
        obj = await self.get_by_id(id)
        if not obj:
            return None

        for key, value in update_data.items():
            setattr(obj, key, value)

        await obj.save()
        return obj

    async def delete(self, id: str) -> bool:
        obj = await self.get_by_id(id)
        if not obj:
            return False

        await obj.delete()
        return True