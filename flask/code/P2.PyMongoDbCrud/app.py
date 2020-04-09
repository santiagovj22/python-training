#Example 2
from bson.objectid import ObjectId
from flask import Flask, jsonify, request

from database.db import get_games_db

app = Flask(__name__)

GAMES_DB = get_games_db('localhost:27017', 'flask', 'flaskpwd')

@app.route('/games')
def get_games():
    games = []
    for game in GAMES_DB.find():
        games.append({'id': str(game['_id']), 'name': game['name'],
                      'genre': game['genre'], 'platforms': game['platforms']})
    return jsonify(games), 200

@app.route('/games/<game_id>')
def get_game_by(game_id):
    game = GAMES_DB.find_one({'_id': ObjectId(game_id)})
    if game is not None:
        game_to_return = {'id': str(game['_id']), 'name': game['name'],
                          'genre': game['genre'], 'platforms': game['platforms']}
        return game_to_return, 200
    return "", 404

@app.route('/games', methods=['POST'])
def add_game():
    game = request.get_json()
    game_id = GAMES_DB.insert_one({'name': game['name'], 'genre': game['genre'],
                                   'platforms': game['platforms']}).inserted_id
    return {'id': str(game_id)}, 201

@app.route('/games/<game_id>', methods=['DELETE'])
def delete_game(game_id):
    deleted = GAMES_DB.delete_one({'_id' : ObjectId(game_id)}).deleted_count
    return '', 204 if (deleted > 0) else 404

@app.route('/games/<game_id>', methods=['PUT'])
def update_game(game_id):
    game = request.get_json()
    updated_game = GAMES_DB.update_one({'_id' : ObjectId(game_id)},
                                       {'$set': {'name': game['name'], 'genre': game['genre'],
                                                 'platforms': game['platforms']}})
    return '', 200 if updated_game.modified_count > 0 else 404

app.run()
