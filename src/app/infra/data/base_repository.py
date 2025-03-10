from abc import ABC
from datetime import datetime
from typing import Any
from sqlalchemy import and_, delete, desc, select, update
from sqlalchemy.orm import Session
from src.app.infra.data.base_model import BaseModel


class BaseRepository(ABC):
    def __init__(self, session: Session, entity_model: BaseModel):
        self.session_db = session
        self.entity_model = entity_model

    async def get_by_id(self, _id: int) -> type[BaseModel] | None:
        statement = select(self.entity_model).where(
            and_(
                self.entity_model.id == _id,
                self.entity_model.deleted_at.is_(None),
            )
        )
        result = await self.session_db.execute(statement=statement)
        result = result.one_or_none()
        if result:
            (result,) = result
        return result
    
    async def get_all(self) -> list[type[BaseModel]] | None:
        statement = (
            select(self.entity_model)
            .where(self.entity_model.deleted_at.is_(None))
            .order_by(desc(self.entity_model.id))
        )
        result = await self.session_db.execute(statement=statement)
        result = result.scalars().all()
        return result
    
    async def get_all_deleted(self) -> list[type[BaseModel]] | None:
        statement = (
            select(self.entity_model)
            .where(self.entity_model.deleted_at.is_not(None))
            .order_by(desc(self.entity_model.id))
        )
        result = await self.session_db.execute(statement=statement)
        result = result.scalars().all()
        return result
    
    async def save(self, model: type[BaseModel]) -> type[BaseModel]:
        self.session_db.add(model)
        await self.session_db.flush()
        await self.session_db.refresh(instance=model)
        return model
    
    async def update_by_id(self, _id: int, values: dict[str, Any]) -> tuple[Any] | None:
        statement = (
            update(self.entity_model)
            .where(self.entity_model.id == _id)
            .values(**values)
        )
        await self.session_db.execute(statement=statement)
        await self.session_db.flush()

    async def hard_delete(self, model: type[BaseModel]) -> None:
        statement = delete(self.entity_model).where(self.entity_model.id == model.id)
        await self.session_db.execute(statement=statement)
        await self.session_db.flush()

    async def soft_delete(self, model: type[BaseModel]) -> None:
        statement = (
            update(self.entity_model)
            .where(self.entity_model.id == model.id)
            .values({"deleted_at": datetime.utcnow()})
        )
        await self.session_db.execute(statement=statement)
        await self.session_db.flush()

    async def force_commit(self) -> None:
        await self.session_db.commit()
        
    async def refresh(self, model: type[BaseModel]) -> None:
        await self.session_db.refresh(instance=model)