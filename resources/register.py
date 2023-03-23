import json
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

from models.credentials import Credentials

# /register:id
class Register(Resource):
    def get(self):
        try:
            limit = request.args.get("limit", 25)
            skip = request.args.get("skip", 0)
            
            credentials = []
            for credential in Credentials.objects().skip(skip).limit(limit):
                credentials.append({
                    "id": str(credential.id),
                    "email": credential.email,
                    "fullName": credential.fullName,
                    "phoneNumber": credential.phoneNumber,
                    "role": credential.role,
                    "isConfirmed": credential.isConfirmed
                })

            return {
                "success": True,
                "credentials": credentials
            }
        except Exception as e:
            return { "success": False, "error": str(e) }

    def post(self):
        data = request.get_json() if request.get_json() else {}

        try:
            new_credential = Credentials(**data)
            new_credential.save()

            print(new_credential, new_credential.to_dict(), new_credential.to_json())

            return {
                "success": True,
                # "credential": new_credential.to_json(),
                "message": "Your account has been successfully created!"
            }
        except Exception as e:
            return { "success": False, "error": str(e) }
    