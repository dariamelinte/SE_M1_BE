import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_register(client):
    payload = {
        "username": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 200
    assert response.json["success"] == True
    assert response.json["message"] == "User created successfully."

    response = client.post("/register", json=payload)
    assert response.status_code == 409
    assert response.json["success"] == False
    assert response.json["message"] == "User already exists."
