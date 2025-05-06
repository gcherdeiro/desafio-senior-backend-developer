from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# Configuração do banco de dados MySQL
DATABASE_URL = "mysql+pymysql://root:testeSenhaInfinita@localhost:3306/carteira_digital"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à sua API FastAPI!"}