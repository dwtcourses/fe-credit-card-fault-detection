# flask_graphene_mongo/models.py
from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField,
    ReferenceField,
    StringField,
    BooleanField,
)


class Card(Document):
    meta = {'collection': 'card'}
    idNumber = StringField()
    name = StringField()
    dob = StringField()
    address = StringField()
    hometown = StringField()
    cardName = StringField()
    isFake = BooleanField()
    # image = StringField()