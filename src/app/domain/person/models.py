from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from src.app.infra.data.base_model import BaseModel


class PersonModel(BaseModel):
    __tablename__ = 'persons'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    document: Mapped[str] = mapped_column(nullable=False, index=True)
    first_name: Mapped[str | None] = mapped_column()
    last_name: Mapped[str | None] = mapped_column()
    email: Mapped[str | None] = mapped_column()
    birth_date: Mapped[date | None] = mapped_column()
    phone: Mapped[str | None] = mapped_column()
   
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
