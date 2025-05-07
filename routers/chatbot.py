from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette import status
from sqlalchemy.orm import Session

from database import SessionLocal
from routers.auth import get_current_user
from routers.documents import get_cnh, get_cpf, get_documents, get_rg, get_vaccination_card
from routers.transport import get_transport_balance

router = APIRouter(
    prefix="/chatbot",
    tags=["chatbot"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.post(
        "/",
        summary="Chatbot",
        description="Interage com o chatbot para obter informações sobre documentos e saldo de transporte.", 
        status_code=status.HTTP_200_OK)
async def chatbot(
    question: str,
    db: db_dependency,
    current_user: user_dependency
):
    if "ola" in question.lower():
        response = "Olá! Como posso ajudar você hoje?"
    elif "tchau" in question.lower():
        response = "Tchau! Tenha um ótimo dia!"
    elif any(keyword in question.lower() for keyword in ["document", "doc", "documento"]):
        return await get_documents(db=db, current_user=current_user)
    elif any(keyword in question.lower() for keyword in ["cpf", "c.p.f"]):
        return await get_cpf(db=db, current_user=current_user)
    elif any(keyword in question.lower() for keyword in ["rg", "r.g", "identidade"]):
        return await get_rg(db=db, current_user=current_user)
    elif any(keyword in question.lower() for keyword in ["vacina", "vacinação", "vaccination"]):
        return await get_vaccination_card(db=db, current_user=current_user)
    elif any(keyword in question.lower() for keyword in ["cnh", "carteira de motorista"]):
        return await get_cnh(db=db, current_user=current_user)
    elif any(keyword in question.lower() for keyword in ["saldo", "balance"]):
        return await get_transport_balance(db=db, current_user=current_user)
    else:
        response = "Desculpe, não entendi sua pergunta. Pode reformular?"

    return JSONResponse(content={"response": response})