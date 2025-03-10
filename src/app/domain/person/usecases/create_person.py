from src.app.domain.person.schemas import PersonCreateSchema
from src.app.infra.data.person.repository import PersonRepository


class CreatePerson():
    repository: PersonRepository

    async def execute(self, data: PersonCreateSchema):
        pass