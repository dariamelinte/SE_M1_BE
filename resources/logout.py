from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import jwt

from models.users import Users

class Logout(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        try:
            # Decode the JWT token
            payload = jwt.decode(data.get("jwt"), "m1-personal-jwt", algorithms=["HS256"])
    
            user = Users.objects(id=payload["user_id"]).first()

            if user is None:
                return {
                    "success": False,
                    "message": "Invalid token",
                }
            
            user.jwt = None
            user.save()
            
            return {
                "success": True,
                "message": "Logout successful"
            }
        except jwt.ExpiredSignatureError:
            return {
                "success": False,
                "message": "Token has expired"
            }, 500
        except jwt.InvalidTokenError:
            return {
                "success": False,
                "message": "Invalid token"
            }, 500
        except Exception as e:
            return {
                "success": False,
                "message": "Oops, something went wrong, please try again."
            }, 500