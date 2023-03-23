from enum import Enum
from mongoengine import Document, StringField, \
    DateTimeField, EmailField, BooleanField, IntField

class RoleType(Enum):
    ADMIN = "ADMIN"
    PATIENT = "PATIENT"
    DOCTOR = "DOCTOR"
    NURSE = "NURSE"

class Credentials(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    firstName = StringField(required=True)
    lastName = StringField(required=True)
    dateOfBirth = DateTimeField(required=False, trim=True)
    phoneNumber = StringField(required=True, trim=True) 
    role = StringField(required=True, choices=[role.value for role in RoleType], default=RoleType.PATIENT.value)
    isConfirmed = BooleanField(required=True, default=False)
    jwt = StringField()
    