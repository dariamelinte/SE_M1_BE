from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import hashlib
from models.users import Users

# /doctors
class Doctors(Resource):
    def get(self):
        try:
            users = list(Users.objects(role="DOCTOR"))
            data = []

            for user in users:
                data.append({
                    "id": str(user.id),
                    "email": user.email,
                    "phoneNumber": user.phoneNumber,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "isConfirmed": user.isConfirmed,
                    "specialisation": {
                        "name": user.specialisation.name
                    }
                })

            return {
                "success": True,
                "message": "Doctors fetched.",
                "data": data
            }
        except Exception as e :
            return {
                "success": False,
                "message": "Doctors not found.",
                "error" : str(e)
            }
        
    def put(self):
        data = request.get_json() if request.get_json() else {}

        id = data.get('id')
        isAccepted = data.get('isAccepted')

        user = Users.objects.get(id=id)

        if isAccepted:
            user.isConfirmed = True
            user.role = "DOCTOR"
        else:
            user.role = "PATIENT"
            user.specialisation = None
        
        user.save()
        user = Users.objects.get(id=id)
        
        return {      
            "success": True,
            "message": "Successfully updated.",
            "user": {
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