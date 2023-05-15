from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import hashlib
from models.users import Users

# /patients
class Patients(Resource):
    def get(self):
        try:
            users = list(Users.objects(role="PATIENT"))
            data = []

            for user in users:
                data.append({
                    "id": str(user.id),
                    "email": user.email,
                    "phoneNumber": user.phoneNumber,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "isConfirmed": user.isConfirmed,
                })

            return {
                "success": True,
                "message": "Patients fetched.",
                "data": data
            }
        except Exception as e :
            return {
                "success": False,
                "message": "Patients not found.",
                "error" : str(e)
            }