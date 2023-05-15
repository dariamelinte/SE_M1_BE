import json
import pytest
from flask import Flask
from unittest.mock import patch
from app import app
from models.users import Users

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_register_success(client):
    data = {
        "email": "test-10@medconnect.com",
        "password": "Test123",
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "1990-01-01",
        "phoneNumber": "555-555-5555",
        "role": "PATIENT"
    }

    response = client.post('/register', json=data)

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert data["success"] == True
    assert data["message"] == "Your account has been successfully created!"
    
    user = data["user"]
    assert "id" in user
    assert "email" in user
    assert "isConfirmed" in user
    assert "firstName" in user
    assert "lastName" in user
    assert "dateOfBirth" in user
    assert "phoneNumber" in user
    assert "role" in user


def test_register_failure(client):
    data = {
        "email": "ttest-10@medconnect.com",
        "password": "Test123",
    }

    response = client.post('/register', json=data)

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert data["success"] == False
    assert "error" in data
