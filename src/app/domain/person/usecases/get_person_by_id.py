from src.app.domain.person.exceptions import PersonNotFoundException
from src.app.domain.person.models import PersonModel
from src.app.domain.person.schemas import PersonCreateSchema, PersonViewSchema
from src.app.infra.data.person.repository import PersonRepository


class GetPersonById():
    def __init__(self, repository: PersonRepository):
        self.repository = repository

    async def execute(self, _id: int) -> PersonViewSchema:
        person: PersonModel | None = await self.repository.get_by_id(_id = _id)
        if not person:
            raise PersonNotFoundException()
        return person