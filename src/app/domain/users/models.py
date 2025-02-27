from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.app.infra.data.base_model import BaseModel
from src.app.domain.person.models import PersonModel


class UserModel(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_name: Mapped[str | None] = mapped_column()
    login_password: Mapped[str | None] = mapped_column()
    transfer_password: Mapped[str | None] = mapped_column()
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'), primary_key=True)
    person: Mapped['PersonModel'] = relationship(  # noqa: F821
        back_populates='registers',
        lazy='joined',
    )