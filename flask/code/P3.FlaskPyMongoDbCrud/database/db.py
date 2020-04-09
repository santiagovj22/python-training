from flask_pymongo import PyMongo
from bson import ObjectId

def get_db(app):
    mongo = PyMongo(app)
    games = mongo.db.get_collection('games')
    def get_games():
        return [row for row in games.find()]

    def get_game(_id):
        return games.find_one({'_id': ObjectId(_id)})

    def insert_game(game):
        new_id = games.insert_one(game).inserted_id
        return str(new_id)

    def delete_game(_id):
        return games.delete_one({'_id': ObjectId(_id)}).deleted_count

    def update_game(_id, game):
        return games.update_one({'_id' : ObjectId(_id)},
                                {'$set': {'name': game['name'], 'genre': game['genre'],
                                          'platforms': game['platforms']}}).modified_count

    return get_games, get_game, insert_game, delete_game, update_game
