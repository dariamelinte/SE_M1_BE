from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import hashlib
from models.users import Users
import jwt
from datetime import datetime, timedelta

class Login(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        password = data.pop('password')

        password_bytes = password.encode('utf-8')
        hash_256 = hashlib.sha256()
        hash_256.update(password_bytes)
        data['password'] = hash_256.hexdigest()

        try:
            user = Users.objects(**data).first()

            if user is None:
                return {
                    "success": False,
                    "message": "Email or password incorrect.",
                }

            token_payload = {
                'id': str(user.id),
                'expirationTime': datetime.utcnow() + timedelta(hours=1)
            }
            token = jwt.encode(token_payload, 'm1_token', algorithm='HS256')
        
            return {
                "success": True,
                "message": "Completely logged in.",
                "user": {
                    "id": str(user.id),
                    "email": user.email,
                    "isConfirmed": user.isConfirmed,
                    "jwt": token,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "dateOfBirth": user.dateOfBirth,
                    "phoneNumber": user.phoneNumber,
                    "role": user.role
                }  
            } 
        except Exception as e :
            return {
                "success": False,
                "message": "Oops, something went wrong, please try again.",
                "error" : str(e)
            }
