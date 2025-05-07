import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_user_password_length():
    # Teste com senha menor que 6 caracteres
    short_password_data = {
        "username": "testuser1",
        "password": "12345"
    }
    response = client.post("/auth/", json=short_password_data)
    assert response.status_code == 422

    # Teste com senha maior que 30 caracteres
    long_password_data = {
        "username": "testuser2",
        "password": "a" * 31
    }
    response = client.post("/auth/", json=long_password_data)
    assert response.status_code == 422

    # Teste com senha válida
    valid_password_data = {
        "username": "testuser3",
        "password": "validpassword123"
    }
    response = client.post("/auth/", json=valid_password_data)
    assert response.status_code == 201