import hashlib
from flask import request
from flask_restful import Resource

from models.credentials import Credentials

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
                    "firstName": credential.firstName,
                    "lastName": credential.lastName,
                    "phoneNumber": credential.phoneNumber,
                    "role": credential.role,
                    "isConfirmed": credential.isConfirmed
                })

            return {
                "success": True,
                "message": "Credentials have been successfully fetched!",
                "credentials": credentials
            }
        except Exception as e:
            return { "success": False, "error": str(e) }

    def post(self):
        data = request.get_json() if request.get_json() else {}
        password = data.pop('password')
        password_bytes = password.encode('utf-8')
        
        hash_256 = hashlib.sha256()
        hash_256.update(password_bytes)
        data['password'] = hash_256.hexdigest()

        try:
            new_credential = Credentials(**data)
            new_credential.save()

            return {
                "success": True,
                "message": "Your account has been successfully created!",
                "credential": {
                    "id": str(new_credential.id),
                    "email": new_credential.email,
                    "phoneNumber": new_credential.phoneNumber,
                    "firstName": new_credential.firstName,
                    "lastName": new_credential.lastName,
                    "password": new_credential.password,
                    "isConfirmed": new_credential.isConfirmed,
                    "role": new_credential.role,
                }
            }
        except Exception as e:
            return { "success": False, "error": str(e) }
    