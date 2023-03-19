import json
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS


# /register
class Register(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        email = json.load('email')
        password = json.load('password')
        role = json.load('role')
        birthdate = json.load('birthdate')
        gender = json.load('gender')
        messageKey = "Congratulations! Your account has been successfully created!"
        print(email)
        print(password)
        print(role)
        print(birthdate)
        print(gender)

        return {      
            "success": True,
            "message": messageKey,
            "account": {
                
            }
        }