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
        }