from typing import List

import bson
from flask_mongoengine import MongoEngine

from persistence.models import Games

__Mongo_DB__ = MongoEngine()

def init_db(app):
    __Mongo_DB__.init_app(app)

def get_all()->List[Games]:
    return Games.objects()

def get_one(_id):
    return Games.objects.get(id=bson.objectid.ObjectId(_id))

def add(game):
    new_game = Games(**game).save()
    return new_game.id

def remove(_id):
    Games.objects.get(id=bson.objectid.ObjectId(_id)).delete()
    return 1

def update(_id, game):
    Games.objects.get(id=bson.objectid.ObjectId(_id)).update(**game)
    return 1
