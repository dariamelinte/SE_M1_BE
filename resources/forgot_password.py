from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS


# /forgot_password
class ForgotPassword(Resource):
    def post(self):
        # data = request.get_json() if request.get_json() else {}
        # email = data.get('email')
        # messageKey = "An email has been sent to your address"

        # print(email)

        return {
            "success": True,
            "message": messageKey,
            "account": {
                "email": email
            }
        }