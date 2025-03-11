from sqlalchemy import and_, select
from src.app.domain.person.models import PersonModel
from src.app.infra.data.base_repository import BaseRepository

class PersonRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session=session, entity_model=PersonModel)
        self.entity_model=PersonModel
        
    async def get_by_document(self, document: str) -> PersonModel | None:
        statement = select(self.entity_model).where(
            and_(
                self.entity_model.document == document,
                self.entity_model.deleted_at.is_(None),
            )
        )
        result = await self.session_db.execute(statement=statement)
        result = result.one_or_none()
        if result:
            (result,) = result
        return result   
    