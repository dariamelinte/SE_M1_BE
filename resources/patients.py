from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import hashlib
from models.credentials import Credentials

# /patients
class Patients(Resource):
    def get(self):
        try:
            credentials = list(Credentials.objects(role="PATIENT"))
            data = []

            for credential in credentials:
                data.append({
                    "id": str(credential.id),
                    "email": credential.email,
                    "phoneNumber": credential.phoneNumber,
                    "firstName": credential.firstName,
                    "lastName": credential.lastName,
                    "isConfirmed": credential.isConfirmed,
                })

            return {
                "success": True,
                "message": "Patients credentials fetched.",
                "data": data
            }
        except Exception as e :
            return {
                "success": False,
                "message": "Credentials not found.",
                "error" : str(e)
            }