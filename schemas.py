from pydantic import BaseModel
from datetime import date

class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class CreateDocumentRequest(BaseModel):
    id: int
    number: str
    name: str
    issued_by: str
    issued_date: date

class CreateCpfRequest(CreateDocumentRequest):
    pass

class CreateRgRequest(CreateDocumentRequest):
    pass

class CreateCnhRequest(CreateDocumentRequest):
    uf: str
    expiration_date: date
    category: str

class CreateVaccinationCardRequest(CreateDocumentRequest):
    birth_date: date
    expiration_date: date
    gender: str