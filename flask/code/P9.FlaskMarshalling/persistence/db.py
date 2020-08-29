import logging

from persistence.mongo_db import DatabaseConnection

__DB = DatabaseConnection()

LOG = logging.getLogger('Games DB')

def init_db(app):
    __DB.init_db(app)

def get_games_collection():
    return __DB.get_collection('games')
