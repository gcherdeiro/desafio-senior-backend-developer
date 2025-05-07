from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
import routers.auth as auth
import routers.documents as documents
from routers.auth import get_current_user
from database import SessionLocal

app = FastAPI()
app.include_router(auth.router)
app.include_router(documents.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado.")
    return {"User": user}