from enum import Enum
from mongoengine import Document, StringField

class RoleType(Enum):
    ADMIN  = "ADMIN"


class Credential(Document):
    email = StringField(required=True, unique=True)
    password = StringField(required=True)

    
