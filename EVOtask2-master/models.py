from mongoengine import Document, StringField


class Person(Document):
    epithet = StringField(required=True)
    name = StringField(required=True)


class Epithet(Document):
    epithet = StringField(required=True)
