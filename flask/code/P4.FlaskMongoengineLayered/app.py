#Example 4
import json
from flask import Flask, request, Response
#from services.stubGamesService import get_service
from services.games_service import get_service

app = Flask(__name__)

MONGO_CNX = 'mongodb://root:jala@localhost:27017/gamestore?authSource=gamestore'

app.config['MONGODB_SETTINGS'] = {'host': MONGO_CNX}

get_all_games, get_game, remove_game, change_game, insert_game = get_service(app)

@app.route('/games')
def get_games():
    games = get_all_games()
    return Response(json.dumps(games, default=str), mimetype="application/json", status=200)

@app.route('/games/<game_id>')
def get_game_by(game_id):
    game = get_game(game_id)
    if game is not None:
        return Response(json.dumps(game, default=str), mimetype="application/json", status=200)
    else:
        return Response('', mimetype="application/json", status=404)

@app.route('/games', methods=['POST'])
def add_game():
    game = request.get_json()
    game_id = insert_game(game)
    return Response({'id': str(game_id)}, mimetype="application/json", status=201)

@app.route('/games/<game_id>', methods=['DELETE'])
def delete_game(game_id):
    deleted = remove_game(game_id)
    return '', 204 if (deleted > 0) else 404

@app.route('/games/<game_id>', methods=['PUT'])
def update_game(game_id):
    game = request.get_json()
    updated = change_game(game_id, game)
    return '', 200 if updated > 0 else 404

app.run()
