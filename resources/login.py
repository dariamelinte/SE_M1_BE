from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import datetime
import jwt
import hashlib

from models.users import Users

class Login(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        password = data.pop('password')

        password_bytes = password.encode('utf-8')
        hash_256 = hashlib.sha256()
        hash_256.update(password_bytes)
        data['password'] = hash_256.hexdigest()

        try:
            user = Users.objects(**data).first()

            if user is None:
                return {
                    "success": False,
                    "message": "Email or password incorrect.",
                }
            # Get the current time
            current_time = datetime.datetime.now()
            # Add one hour to the current time
            one_hour_later = current_time + datetime.timedelta(hours=1)
            
            # Define the payload (claims) for the JWT
            payload = {
                "user_id": str(user.id),
                "expiration_time": one_hour_later.timestamp()
            }

            # Encode the payload and sign it with the secret key to create the JWT
            user.jwt = jwt.encode(payload, "m1-personal-jwt", algorithm="HS256")
            user.save()
        
            return {
                "success": True,
                "message": "Completely logged in.",
                "user": {
                    "id": str(user.id),
                    "email": user.email,
                    "isConfirmed": user.isConfirmed,
                    "jwt": user.jwt,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "dateOfBirth": str(user.dateOfBirth),
                    "phoneNumber": user.phoneNumber,
                    "role": user.role
                }  
            } 
        except Exception as e :
            return {
                "success": False,
                "message": "Oops, something went wrong, please try again.",
                "error" : str(e)
            }
