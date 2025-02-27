import asyncio
from src.app.domain.person.models import PersonModel
from src.app.domain.users.models import UserModel
from src.app.environment import settings
from src.app.infra.data.database import async_engine
from src.app.infra.data.base_model import BaseModel


async def create_tables():
    print('Criando tabelas no banco de dados!')
    print(f'{settings.database_settings.database_sync_uri}')
    async with async_engine.begin() as engine:
        await engine.run_sync(lambda engine: BaseModel.metadata.drop_all(engine))
        await engine.run_sync(lambda engine: BaseModel.metadata.create_all(engine))
    print('Todas tabelas criadas com sucesso!')
async def main():
    await create_tables()
if __name__ == "__main__":
    asyncio.run(main())
    