import threading
import bson

from flask_mongoengine import MongoEngine

__Mongo_DB__ = MongoEngine()
__lock__ = threading.Lock()
__Instance__ = {'configured': False}

def init_db(app):
    with __lock__:
        if not __Instance__['configured']:
            __Instance__['configured'] = True
            __Mongo_DB__.init_app(app)
            print("Mongo DB configured!")
        else:
            print("Mongo Db already configured...")

def to_object_id(id_str):
    return bson.objectid.ObjectId(id_str)
