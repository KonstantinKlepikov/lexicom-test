from typing import TypeVar, Generic, Type
from pydantic import BaseModel
from redis.asyncio import Redis


SchemaDbType = TypeVar("SchemaDbType", bound=BaseModel)
SchemaReturnType = TypeVar("SchemaReturnType", bound=BaseModel)


class CRUDBase(Generic[SchemaDbType]):
    """Base class for redis crud
    """

    def __init__(self, schema: Type[SchemaReturnType]) -> None:
        """
        CRUD object with default methods to Create,
        Read, Update, Delete (CRUD).
        """
        self.schema = schema

    async def get(self, uuid_id: str, db: Redis) -> SchemaReturnType:
        """Get single document

        Args:
            uuid_id (str): uuid id
            db (Redis): db connection

        Returns:
            SchemaReturnType: search result
        # TODO: test me
        """
        result = await db.hget(uuid_id)
        return self.schema(**result)

    async def create(
        self,
        uuid_id: str,
        db: Redis,
        obj_in: SchemaDbType
            ) -> None:
        """Create document

        Args:
            uuid_id (str): uuid id
            db (Redis): db connection
            obj_in (SchemaDbType): scheme to creare
        # TODO: test me
        """
        await db.hmset(uuid_id, obj_in.model_dump())

    async def update(
        self,
        uuid_id: str,
        db: Redis,
        obj_in: dict[str, int | str]
            ) -> None:
        """Update document fields

        Args:
            uuid_id (str): uuid id
            db (Redis): db connection
            obj_in (dict[str, int | str]): fields to update
        # TODO: test me
        """
        await db.hmset(uuid_id, obj_in)

    async def delete(self, uuid_id: str, db: Redis) -> None:
        """Remove one document

        Args:
            uuid_id (str): uuid id
            db (Redis): db connection
        # TODO: test me
        """
        await db.delete(uuid_id)
