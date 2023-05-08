from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import jwt

class Logout(Resource):
    def post(self):
        token = request.headers.get('Authorization')
        if not token:
            return {"success": False, "message": "No token provided."}, 401

        try:
            decoded_token = jwt.decode(token, 'your_secret_key_here', algorithms=['HS256'])
            return {"success": True, "message": "Logged out successfully."}, 200
        except jwt.ExpiredSignatureError:
            return {"success": False, "message": "Signature expired. Please log in again."}, 401
        except jwt.InvalidTokenError:
            return {"success": False, "message": "Invalid token. Please log in again."}, 401