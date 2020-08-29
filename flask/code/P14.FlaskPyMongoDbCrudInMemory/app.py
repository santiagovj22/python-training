#Example 3
import json

from flask import Flask, request, Response

from database.db import get_db

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://flask:flaskpwd@localhost:27017/gamestore?authSource=gamestore'

get_all, get_game, insert_game, remove_game, change_game = get_db(app)

@app.route('/games')
def get_games():
    games = get_all()
    return Response(json.dumps(games, default=str), mimetype="application/json", status=200)

@app.route('/games/<game_id>')
def get_game_by(game_id):
    game = get_game(game_id)
    if game is not None:
        return Response(json.dumps(game, default=str), mimetype="application/json", status=200)
    else:
        return '', 404

@app.route('/games', methods=['POST'])
def add_game():
    game = request.get_json()
    game_id = insert_game(game)
    result = json.dumps({'id': game_id})
    return Response(result, mimetype="application/json", status=200)

@app.route('/games/<game_id>', methods=['DELETE'])
def delete_game(game_id):
    deleted = remove_game(game_id)
    return '', 204 if (deleted > 0) else 404

@app.route('/games/<game_id>', methods=['PUT'])
def update_game(game_id):
    game = request.get_json()
    updated = change_game(game_id, game)
    return '', 200 if updated > 0 else 404

app.run(debug=False)
