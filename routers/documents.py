from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from database import SessionLocal
from sqlalchemy.orm import Session
from models import Cnh, Cpf, Documents, Rg, VaccinationCard
from routers.auth import get_current_user
from schemas import CreateCpfRequest, CreateRgRequest, CreateCnhRequest, CreateVaccinationCardRequest

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/", status_code=status.HTTP_200_OK)
async def get_documents(
    db: db_dependency,
    current_user: user_dependency
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado."
        )

    user_id = current_user.get("id")
    document = db.query(Documents).filter(Documents.user_id == user_id).first()

    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum documento encontrado para o usuário."
        )
    
    return {
        "documents": {
            "cpf": document.cpf,
            "rg": document.rg,
            "cnh": document.cnh,
            "vaccination_card": document.vaccination_card
        }
    }

@router.post("/cpf", status_code=status.HTTP_201_CREATED)
async def create_cpf(create_cpf_request: CreateCpfRequest,
                    db: db_dependency,
                    current_user: user_dependency):
    
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado."
        )
    
    create_cpf_model = Cpf(
        number=create_cpf_request.number,
        name=create_cpf_request.name,
        issued_by=create_cpf_request.issued_by,
        issued_date=create_cpf_request.issued_date
    )

    db.add(create_cpf_model)
    db.commit()
    db.refresh(create_cpf_model)  

    
    user_id = current_user.get("id") 
    document = db.query(Documents).filter(Documents.user_id == user_id).first()

    if not document:
        document = Documents(user_id=user_id, cpf_id=create_cpf_model.id)
        db.add(document)
    else:
        document.cpf_id = create_cpf_model.id

    db.commit()

    return {"message": "CPF criado e associado aos documentos com sucesso."}

@router.post("/rg", status_code=status.HTTP_201_CREATED)
async def create_rg(create_rg_request: CreateRgRequest,
                    db: db_dependency,
                    current_user: user_dependency):
    
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado."
        )
    
    create_rg_model = Rg(
        number=create_rg_request.number,
        name=create_rg_request.name,
        issued_by=create_rg_request.issued_by,
        issued_date=create_rg_request.issued_date
    )

    db.add(create_rg_model)
    db.commit()
    db.refresh(create_rg_model)  

    
    user_id = current_user.get("id") 
    document = db.query(Documents).filter(Documents.user_id == user_id).first()

    if not document:
        document = Documents(user_id=user_id, rg_id=create_rg_model.id)
        db.add(document)
    else:
        document.rg_id = create_rg_model.id

    db.commit()

    return {"message": "RG criado e associado aos documentos com sucesso."}

@router.post("/cnh", status_code=status.HTTP_201_CREATED)
async def create_cnh(create_cnh_request: CreateCnhRequest,
                    db: db_dependency,
                    current_user: user_dependency):
    
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado."
        )
    
    create_cnh_model = Cnh(
        number=create_cnh_request.number,
        name=create_cnh_request.name,
        uf=create_cnh_request.uf,
        issued_by=create_cnh_request.issued_by,
        issued_date=create_cnh_request.issued_date,
        expiration_date=create_cnh_request.expiration_date,
        category=create_cnh_request.category
    )

    db.add(create_cnh_model)
    db.commit()
    db.refresh(create_cnh_model)  

    
    user_id = current_user.get("id") 
    document = db.query(Documents).filter(Documents.user_id == user_id).first()

    if not document:
        document = Documents(user_id=user_id, cnh_id=create_cnh_model.id)
        db.add(document)
    else:
        document.cnh_id = create_cnh_model.id

    db.commit()

    return {"message": "CNH criada e associada aos documentos com sucesso."}

@router.post("/vaccination_card", status_code=status.HTTP_201_CREATED)
async def create_vaccination_card(create_vaccination_card_request: CreateVaccinationCardRequest,
                                   db: db_dependency,
                                   current_user: user_dependency):
    
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado."
        )
    
    create_vaccination_card_model = VaccinationCard(
        number=create_vaccination_card_request.number,
        name=create_vaccination_card_request.name,
        birth_date=create_vaccination_card_request.birth_date,
        issued_date=create_vaccination_card_request.issued_date,
        expiration_date=create_vaccination_card_request.expiration_date,
        gender=create_vaccination_card_request)
    
    db.add(create_vaccination_card_model)
    db.commit()
    db.refresh(create_vaccination_card_model)

    user_id = current_user.get("id") 
    document = db.query(Documents).filter(Documents.user_id == user_id).first()

    if not document:
        document = Documents(user_id=user_id, vaccination_card_id=create_vaccination_card_model.id)
        db.add(document)
    else:
        document.vaccination_card_id = create_vaccination_card_model.id

    db.commit()

    return {"message": "Carteira de vacinação criada e associada aos documentos com sucesso."}