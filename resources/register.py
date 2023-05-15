import hashlib
from flask import request
from flask_restful import Resource

from models.users import Users

class Register(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        password = data.pop('password')
        password_bytes = password.encode('utf-8')
        
        hash_256 = hashlib.sha256()
        hash_256.update(password_bytes)
        data['password'] = hash_256.hexdigest()

        try:
            print(data)
            new_user = Users(**data)
            print(new_user)
            new_user.save()

            return {
                "success": True,
                "message": "Your account has been successfully created!",
                "user": {
                    "id": str(new_user.id),
                    "email": new_user.email,
                    "isConfirmed": new_user.isConfirmed,
                    "firstName": new_user.firstName,
                    "lastName": new_user.lastName,
                    "dateOfBirth": str(new_user.dateOfBirth),
                    "phoneNumber": new_user.phoneNumber,
                    "role": new_user.role
                }  
            }
        except Exception as e:
            return { "success": False, "error": str(e) }
    