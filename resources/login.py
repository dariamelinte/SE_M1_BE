from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import hashlib
from models.credentials import Credentials
import jwt
from datetime import datetime, timedelta

class Login(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        email = data.get('email')
        password = data.pop('password')

        password_bytes = password.encode('utf-8')
        hash_256 = hashlib.sha256()
        hash_256.update(password_bytes)
        data['password'] = hash_256.hexdigest()

        try:
            credential = Credentials.objects(**data).first()

            if credential is not None:
                token_payload = {
                    'user_id': str(credential.id),
                    'exp': datetime.utcnow() + timedelta(hours=1)
                }
                token = jwt.encode(token_payload, 'your_secret_key_here', algorithm='HS256')
                return {
                    "success": True,
                    "message": "Completely logged in.",
                    "credential": {
                        "id": str(credential.id),
                        "email": credential.email,
                        "phoneNumber": credential.phoneNumber,
                        "firstName": credential.firstName,
                        "lastName": credential.lastName,
                        "password": credential.password,
                        "isConfirmed": credential.isConfirmed,
                        "role": credential.role,
                    },
                    "jwt": token.decode('utf-8')
                }
            
            return {
                "success": False,
                "message": "Credentials not found.",
            }
        except Exception as e :
            return {
                "success": False,
                "message": "Credentials not found.",
                "error" : str(e)
            }
