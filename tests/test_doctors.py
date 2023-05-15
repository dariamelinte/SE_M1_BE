import json
import pytest
from app import app
from unittest.mock import patch
from models.users import Users

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_doctors_success(client):
    # Send GET request to the doctors endpoint
    response = client.get('/doctors')

    # Assert the response status
    assert response.status_code == 200
    assert response.content_type == 'application/json'

    # Parse the response data
    data = json.loads(response.data)

    # Assert the response data
    assert data["success"] == True
    assert data["message"] == "Doctors fetched."
    assert len(data["data"]) > 0


def test_update_doctor_failure(client):
    data = {
        "id": "64626a297e9fa38d4e6425fb",
        "isAccepted": False
    }

    # Send PUT request to the doctors endpoint
    response = client.put('/doctors', json=data)

    # Assert the response status
    assert response.status_code == 200
    assert response.content_type == 'application/json'

    # Parse the response data
    data = json.loads(response.data)

    # Assert the response data
    assert data["success"] == True
    assert data["message"] == "Successfully updated."

    # Assert the updated user data in the response
    updated_user_data = data["user"]
    assert updated_user_data["id"] == "64626a297e9fa38d4e6425fb"
    assert updated_user_data["role"] == "PATIENT"
  

def test_update_doctor_success(client):
    data = {
        "id": "64626a297e9fa38d4e6425fb",
        "isAccepted": True
    }

    # Send PUT request to the doctors endpoint
    response = client.put('/doctors', json=data)

    # Assert the response status
    assert response.status_code == 200
    assert response.content_type == 'application/json'

    # Parse the response data
    data = json.loads(response.data)

    # Assert the response data
    assert data["success"] == True
    assert data["message"] == "Successfully updated."

    # Assert the updated user data in the response
    updated_user_data = data["user"]
    assert updated_user_data["id"] == "64626a297e9fa38d4e6425fb"
    assert updated_user_data["role"] == "DOCTOR"

