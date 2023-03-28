import os
import json
import smtplib
import ssl
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

from email.message import EmailMessage

email_sender = 'medconnect.fii@gmail.com'
email_password = 'dzvwzbfhvwfftbxk'
email_reciever = 'jomirajo@gmail.com'

subject = 'Password recovery email'
body = """ Access the following link in order to recover/change your account password: """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())


# /forgot_password
class ForgotPassword(Resource):
    def post(self):
        data = request.get_json() if request.get_json() else {}
        email = data.get('email')
        messageKey = "An email has been sent to your address!"

        print(email)

        return {
            "success": True,
            "message": messageKey,
            "account": {
                "email": email
            }
        }
