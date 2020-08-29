from flask_mongoengine import mongoengine as me

class Games(me.Document):
    name = me.StringField(required=True, unique=True)
    genre = me.StringField(required=True, unique=False)
    platforms = me.ListField(me.StringField(), required=False)
    created_by = me.StringField(required=True)
    liked_by = me.ListField(me.StringField(), required=False)
    

    def as_dict(self):
        return {'id': str(self._object_key['pk']), 'name': self.name,
                'created_by': self.created_by,
                'genre': self.genre, 'platforms': self.platforms, 'liked_by': self.liked_by}


class Users(me.Document):
    name = me.StringField(required=True, unique=True)
    password = me.StringField(required=True)

    def as_dict(self):
        return {'id': str(self._object_key['pk']), 'name': self.name}
