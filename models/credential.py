from enum import Enum
from mongoengine import Document, StringField, DateTimeField, EmailField, BooleanField, IntField

class RoleType(Enum):
    ADMIN = "ADMIN"
    PATIENT = "PATIENT"
    DOCTOR = "DOCTOR"
    NURSE = "NURSE"

class Credential(Document):
    id = IntField(primary_key=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    fullName = StringField(required=True)
    dateOfBirth = DateTimeField(required=False, trim=True)
    phoneNumber = StringField(required=True, trim=True) 
    role = StringField(required=True, choices=[role.value for role in RoleType], default=RoleType.PATIENT.value)
    isConfirmed = BooleanField(required=True, default=False)