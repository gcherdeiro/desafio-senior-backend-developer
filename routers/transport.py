from decimal import Decimal
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal
from models import Transport
from routers.auth import get_current_user


router = APIRouter(
    prefix="/transport",
    tags=["transport"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get(
        "/balance", 
        summary="Obter saldo de transporte",
        description="Retorna o saldo de transporte do usuário autenticado.",
        status_code=status.HTTP_200_OK)
async def get_transport_balance(
    db: db_dependency,
    current_user: user_dependency
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado."
        )

    user_id = current_user.get("id")
    transport = db.query(Transport).filter(Transport.user_id == user_id).first()

    if not transport:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum saldo encontrado para o usuário."
        )
    
    return {"message": "Saldo atual: R$ " + str(transport.balance)}

@router.post(
        "/add_balance", 
        summary="Adicionar saldo de transporte",
        description="Adiciona um valor ao saldo de transporte do usuário autenticado.",
        status_code=status.HTTP_201_CREATED)
async def add_transport_balance(
    db: db_dependency,
    current_user: user_dependency,
    amount: float
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado."
        )

    user_id = current_user.get("id")
    transport = db.query(Transport).filter(Transport.user_id == user_id).first()

    if not transport:
        transport = Transport(
            user_id=user_id,
            balance=Decimal(0.),
            last_transaction_date=None
        )
        db.add(transport)
    
    transport.balance += Decimal(amount)
    db.commit()
    
    return {"message": "Saldo atualizado com sucesso!"}