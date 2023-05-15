from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import jwt

class Logout(Resource):
    def post(self):
        print("logout")
        # token = request.headers.get('Authorization')
        # if not token:
        #     return {"success": False, "message": "No token provided."}, 401

        # try:
        #     return {"success": True, "message": "Logged out successfully."}, 200
        # except jwt.ExpiredSignatureError:
        #     return {"success": False, "message": "Signature expired. Please log in again."}, 401
        # except jwt.InvalidTokenError:
        #     return {"success": False, "message": "Invalid token. Please log in again."}, 401