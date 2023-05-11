import hashlib
import os
from http import client
from email.message import EmailMessage
import smtplib
import ssl
import random
from pymongo import MongoClient
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import pymongo
from dotenv import load_dotenv

load_dotenv()

# /forgot_password
class ForgotPassword(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        email = data.get('email')
        messageKey = "An email has been sent to your address"

        print(email)

        lower="abcdefghijklmnopqrstuvwxyz"
        upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers="0123456789"
        symbols="!@#$%^&*()"

        string=lower+upper+numbers+symbols
        lenght=26
        new_password="".join(random.sample(string,lenght))

        password_bytes = new_password.encode('utf-8')
        hash_256 = hashlib.sha256()
        hash_256.update(password_bytes)
        print("Your new password is:" + new_password)
        new_password = hash_256.hexdigest()
        print("Your new password is:" + new_password)

        email_sender=os.getenv("EMAIL_SENDER")
        email_password=os.getenv("EMAIL_PSWD")
        email_reciever=email

        subject='Password Recovery Email'
        body="Your new password is " + new_password

        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_reciever
        em['Subject']=subject
        em.set_content(body)

        context=ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())


        client=pymongo.MongoClient("mongodb+srv://M1:6bVaKlxPr7RFIY80@db.i0bozci.mongodb.net/?retryWrites=true&w=majority")
        db=client["test"]
        users=db["users"]

        users.update_one({"email":email}, {"$set": {"password": new_password}})

        return {
            "success": True,
            "message": messageKey,
            "account": {
                "email": email
            }
        }
    
