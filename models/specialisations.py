from enum import Enum
from mongoengine import EmbeddedDocument, StringField

class Specialisations(EmbeddedDocument):
    name = StringField(required=True)
