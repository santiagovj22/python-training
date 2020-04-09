from flask_mongoengine import mongoengine as me

class Games(me.Document):
    name = me.StringField(required=True, unique=True)
    genre = me.StringField(required=True, unique=False)
    platforms = me.ListField(me.StringField(), required=False)
