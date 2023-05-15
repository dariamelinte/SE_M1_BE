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

def test_login_successful(client):
    data = {
        "email": "test-patient3@medconnect.com",
        "password": "Test123"
    }

    # Send POST request to the login endpoint
    response = client.post('/login', json=data)

    # Assert the response status code and JSON data
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert data["success"] == True
    assert data["message"] == "Completely logged in."
    
    user = data["user"]
    assert user["email"] == "test-patient3@medconnect.com"
    assert user["phoneNumber"] == "0749639919"
    assert user["firstName"] == "Test"
    assert user["lastName"] == "Test"
    assert user["role"] == "PATIENT"
    assert user["jwt"] is not None

def test_login_incorrect_credentials(client):
    data = {
        "email": "test-patient3@medconnect.com",
        "password": "Test1234"
    }

    response = client.post('/login', json=data)

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert data["success"] == False
    assert data["message"] == "Email or password incorrect."

def test_login_exception(client):
    data = {
        "email": "test-patient3@medconnect.com",
        "password": "Test123"
    }

    # Mock the Users.objects method to raise an exception
    with patch.object(Users, 'objects') as mock_objects:
        mock_objects.return_value.first.side_effect = Exception('Something went wrong')

        response = client.post('/login', json=data)

        assert response.status_code == 200
        assert response.content_type == 'application/json'
        
        data = json.loads(response.data)
        assert data["success"] == False
        assert data["message"] == "Oops, something went wrong, please try again."
        assert data["error"] == "Something went wrong"
