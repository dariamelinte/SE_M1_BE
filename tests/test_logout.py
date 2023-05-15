# import json
# import pytest
# from flask import Flask
# from unittest.mock import patch
# from app import app
# from models.users import Users

# @pytest.fixture
# def client():
#     with app.test_client() as client:
#         yield client


# def test_logout_success(client):
#     user = Users(id="64626bf53c5211d8e106b184", jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjQ2MjZiZjUzYzUyMTFkOGUxMDZiMTg0IiwiZXhwaXJhdGlvbl90aW1lIjoxNjg0MTc1MzY4LjE0NDc1M30.GPzBP3V3d42WI159aayDD9OnAIjEPYWQHuOqtwiwR8k")
#     user.save()

#     data = {
#         "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjQ2MjZiZjUzYzUyMTFkOGUxMDZiMTg0IiwiZXhwaXJhdGlvbl90aW1lIjoxNjg0MTc1MzY4LjE0NDc1M30.GPzBP3V3d42WI159aayDD9OnAIjEPYWQHuOqtwiwR8k"
#     }
    
#     response = client.post('/logout', json=data)

#     assert response.status_code == 200
#     assert response.content_type == 'application/json'

#     data = json.loads(response.data)
#     assert data["success"] == True
#     assert data["message"] == "Logout successful"

#     updated_user = Users.objects(id="64626bf53c5211d8e106b184").first()
#     assert updated_user.jwt is None


# def test_logout_invalid_token(client):
#     data = {
#         "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjQ2MjZiZjUzYzUyMTFkOGUxMDZiMTg0IiwiZXhwaXJhdGlvbl90aW1lIjoxNjg0MTc1MzY4LjE0NDc1M30.GPzBP3V3d42WI159aayDD9OnAIjEPYWQHuOqtwiwR0l"
#     }

#     response = client.post('/logout', json=data)

#     assert response.status_code == 200
#     assert response.content_type == 'application/json'

#     data = json.loads(response.data)
#     assert data["success"] == False
#     assert data["message"] == "Invalid token"


# def test_logout_expired_token(client):
#     expired_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjQ2MjZhN2Y3ZTlmYTM4ZDRlNjQyNWZkIiwiZXhwaXJhdGlvbl90aW1lIjoxNjg0MTgzMTI5LjE3ODM3M30.eO9eKG_s00XAAWO4cJ7AY1XxfQMpmuEvRKg-1E5wgzQ"
#     data = {
#         "jwt": expired_token
#     }

#     response = client.post('/logout', json=data)

#     assert response.status_code == 500
#     assert response.content_type == 'application/json'

#     data = json.loads(response.data)
#     assert data["success"] == False
#     assert data["message"] == "Token has expired"


# def test_logout_exception(client):
#     data = {
#         "jwt": "hello"
#     }

#     # Mock the Users.objects method to raise an exception
#     with patch.object(Users, 'objects') as mock_objects:
#         mock_objects.return_value.first.side_effect = Exception('Something went wrong')

#         response = client.post('/logout', json=data)

#         assert response.status_code == 500
#         assert response.content_type == 'application/json'

#         data = json.loads(response.data)

#         assert data["success"] == False
#         assert data["message"] == "Oops, something went wrong, please try again."
#         assert data["error"] == "Something went wrong"
