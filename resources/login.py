from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import hashlib
from models.credentials import Credentials


# /login:id
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
            credential = Credentials.objects.all
            print (credential)
            
        except Exception as e : 
            return False

        return {
            "success": True,
            "account": {
                "email": email
            }
        }