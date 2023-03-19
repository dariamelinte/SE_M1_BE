<<<<<<< HEAD
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS


# /logout
class Logout(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        id = data.get('id')
        messageKey = "Succesfully logged out!"
        print(id)

        return {      
            "success": True,
            "message": messageKey,
            "account": {
                "id":id
            }
=======
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS


# /logout
class Logout(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        id = data.get('id')

        print(password)

        return {
            "success": True,
            "account": {
                "email": email
            }
>>>>>>> 1751f4e471c8f7bf799b77ed3dece443d7580c96
        }