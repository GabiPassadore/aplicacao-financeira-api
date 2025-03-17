from src.app.domain.person.models import PersonModel
from src.app.domain.person.schemas import PersonCreateSchema, PersonViewSchema
from src.app.infra.data.person.repository import PersonRepository
from src.app.domain.person.exceptions import PersonAlreadyExistsException


class CreatePerson():
    def __init__(self, repository: PersonRepository):
        self.repository = repository
        
    async def execute(self, data: PersonCreateSchema) -> PersonViewSchema:
        if await self.repository.get_by_document(document=data.document):
            raise PersonAlreadyExistsException()
        person_values= {
            'document': data.document,
            'first_name': data.first_name,
            'last_name': data.last_name,
            'email': data.email,
            'birth_date': data.birth_date,
            'phone': data.phone,
        }
        model = PersonModel(**person_values)
        result = await self.repository.save(model=model)  
        await self.repository.force_commit()   
        return result 