from pydantic import BaseModel, Field
from datetime import date

class CreateUserRequest(BaseModel):
    username: str
    password: str = Field(..., min_length=6, max_length=30, description="A senha deve ter entre 6 e 30 caracteres.")

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