from typing import Annotated
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from routers import chatbot, health, transport, auth, documents
from routers.auth import get_current_user
from database import SessionLocal

app = FastAPI(
    title="API de Carteira Digital",
    description="API para gerenciamento de documentos digitais e saldo de transporte público.",
    version="1.0.0",
)
app.include_router(auth.router)
app.include_router(documents.router)
app.include_router(transport.router)
app.include_router(chatbot.router)
app.include_router(health.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]