from enum import Enum
from mongoengine import Document, StringField, \
    DateTimeField, EmailField, BooleanField, IntField

from models.specialisations import Specialisations

class RoleType(Enum):
    ADMIN = "ADMIN"
    PATIENT = "PATIENT"
    DOCTOR = "DOCTOR"

class Users(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    isConfirmed = BooleanField(required=True, default=False)
    jwt = StringField()

    firstName = StringField(required=True)
    lastName = StringField(required=True)
    dateOfBirth = DateTimeField(required=False, trim=True)
    phoneNumber = StringField(required=True, trim=True) 
    role = StringField(required=True, choices=[role.value for role in RoleType], default=RoleType.PATIENT.value)

    cnp = StringField()
    sex = StringField()
    citizenship = StringField()
    country = StringField()
    county = StringField()
    city = StringField()
    completeAddress = StringField()
    lastName = StringField()
    specialisation = Specialisations();
