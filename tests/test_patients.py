import json
import pytest
from app import app
from unittest.mock import patch
from models.users import Users

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_patients_success(client):
    # Send GET request to the patients endpoint
    response = client.get('/patients')

    # Assert the response status
    assert response.status_code == 200
    assert response.content_type == 'application/json'

    # Parse the response data
    data = json.loads(response.data)

    # Assert the response data
    assert data["success"] == True
    assert data["message"] == "Patients fetched."
    assert len(data["data"]) > 0
