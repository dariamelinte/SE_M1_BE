import json
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

from models.credential import Credential

# /register:id
class Register(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        email = data.get('email')
        messageKey = "Your account has been successfully created!"

        try:
            Credential(**data).save()
            credential_created = Credential.objects(email = email).first()
            print(credential_created)

            return {
                "success": True,
                "credential": json.loads(credential_created)
            }
        except Exception as e:
            return { "success": False, "error": str(e) }
        
        return {
            "success": True,
            "message": messageKey,
            "account": {
                "email": email
            }
        }