from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY

class PersonNotFoundException(HTTPException):
    def __init__(self):
        detail = "Person not found"
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail=detail)
        
class PersonAlreadyExistsException(HTTPException):
    def __init__(self):
        detail = "Person already exists"
        super().__init__(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)