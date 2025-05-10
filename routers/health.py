from fastapi import APIRouter
import httpx
from database import SessionLocal
from sqlalchemy import text
from database import engine

router = APIRouter(
    prefix="/health",
    tags=["health"],
)

async def check_database():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception as e:
        return False

async def check_external_service():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://jsonplaceholder.typicode.com/posts')
            return response.status_code == 200
    except:
        return False

@router.get(
        "/", 
        summary="Health Check",
        description="Verifica se a API está funcionando corretamente.",
        status_code=200)
async def health_check():
    db_status = await check_database()
    api_status = await check_external_service()

    return {
        "database": "up" if db_status else "down",
        "external_api": "up" if api_status else "down"
    }