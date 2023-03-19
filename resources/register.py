import json
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS


# /register:id
class Register(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        email = data.get('email')
        password = data.get('password')
        fullName = data.get('fullName')
        dateOfBirth = data.get('dateOfBirth')
        phoneNumber = data.get('phoneNumber')
        messageKey = "Your account has been successfully created!"

        print(password)

        return {
            "success": True,
            "message": messageKey,
            "account": {
                "email": email
            }
        }