from src.app.domain.person.models import PersonModel
from src.app.infra.data.base_repository import BaseRepository

class PersonRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session=session, entity_model=PersonModel)
        self.entity_model=PersonModel
        