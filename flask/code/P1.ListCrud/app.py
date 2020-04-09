#List Crud
from flask import Flask, jsonify, request

app = Flask(__name__)

GAMES = [
    {
        "name": "Pac Man",
        "genre" : "Arcade",
        "platforms": ["PS3", "NINTENDO IO", "ATARI"]
    },
    {
        "name": "Mario Party",
        "genre": "Platform",
        "platforms": ["NINTENDO IO"]
    }
]

@app.route('/games', methods=['POST'])
def add_game():
    game = request.get_json()
    GAMES.append(game)
    return {"index": len(GAMES) - 1}, 200

@app.route('/games/<int:index>', methods=['PUT'])
def update_game(index):
    game = request.get_json()
    GAMES[index] = game
    return jsonify(GAMES[index]), 200

@app.route('/games')
def get_games():
    return jsonify(GAMES)

@app.route('/games/<int:index>')
def get_game_by_id(index):
    return jsonify(GAMES[index])

@app.route('/games/<int:index>', methods=['DELETE'])
def delete_game(index):
    GAMES.pop(index)
    return {}, 200

app.run(debug=True)
