from datetime import datetime
from fastapi_camelcase import CamelModel
from pydantic import EmailStr, field_validator
from src.app.application.common.helpers.cpf import CPFHelper
from src.app.application.common.helpers.phone import PhoneHelpers

class PersonCreateSchema(CamelModel):
    document: str 
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    birth_date: datetime | None = None
    phone: str | None = None
    
    @field_validator('document')
    def validate_document(cls, value: str) -> str:
        if not CPFHelper.validate(value):
            raise ValueError('Invalid CPF')
        return value
    
    @field_validator('phone')
    def validate_phone(cls, value: str) -> str:
        if not PhoneHelpers.validate_phone_number(value):
            raise ValueError('Invalid phone number')
        return value
    
class PersonViewSchema(CamelModel):
    id: int
    document: str
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    birth_date: datetime | None = None
    phone: str | None = None
    full_name: str | None = None
    created_at: datetime
    updated_at: datetime | None = None
    deleted_at: datetime | None = None