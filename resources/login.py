from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS


# /login:id
class Login(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        email = data.get('email')
        password = data.get('password')

        print(password)

        return {
            "success": True,
            "account": {
                "email": email
            }
        }