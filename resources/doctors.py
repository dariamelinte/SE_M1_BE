from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import hashlib
from models.credentials import Credentials

# /doctors
class Doctors(Resource):
    def get(self):
        try:
            credentials = list(Credentials.objects(role="DOCTOR"))
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
    
            print(data)

            return {
                "success": True,
                "message": "Doctors credentials fetched.",
                "data": data
            }
        except Exception as e :
            return {
                "success": False,
                "message": "Credentials not found.",
                "error" : str(e)
            }
        
    def put(self):
        data = request.get_json() if request.get_json() else {}

        id = data.get('id')
        isAccepted = data.get('isAccepted')

        user = Credentials.objects.get(id=id)

        if isAccepted:
            user.isConfirmed = True
            user.role = "DOCTOR"
        else:
            user.role = "PATIENT"
        
        user.save()
        user = Credentials.objects.get(id=id)
        
        return {      
            "success": True,
            "message": "Successfully updated.",
            "account": {
                "id": str(user.id),
                "email": user.email,
                "phoneNumber": user.phoneNumber,
                "firstName": user.firstName,
                "lastName": user.lastName,
                "password": user.password,
                "isConfirmed": user.isConfirmed,
                "role": user.role,
            }
        }