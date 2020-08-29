from flask import request
from flask_restx import Resource

from controllers.models import get_game_model
from services.games_service import add_game, get_games, get_game, delete_game, update_game

def init_games_controller(api):

    game_model = get_game_model(api)

    class GameList(Resource):
        """A resource controller for a collection of games"""
        def get(self):
            return get_games()

        @api.expect(game_model)
        def post(self):
            data = request.get_json()
            game_id = add_game(data)
            return {'id': game_id}, 201
          
    class Game(Resource):
        """A resource controller for a game """
        def get(self, game_id):
            game = get_game(game_id)
            if game is not None:
                return game, 200
            api.abort(504, "Game {} doesn't exist".format(game_id))

        def delete(self, game_id):
            deleted = delete_game(game_id)
            return None, 204 if deleted > 0 else 404

        @api.expect(game_model)
        def put(self, game_id):
            game = request.get_json()
            updated = update_game(game_id, game)
            return None, 200 if updated > 0 else 404

    api.add_resource(GameList, '/games')
    api.add_resource(Game, '/games/<string:game_id>')
