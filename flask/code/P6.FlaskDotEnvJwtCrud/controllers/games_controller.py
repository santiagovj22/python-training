from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource

from services.games_service import init_service, get_games, get_game_by_id, update_game, remove_game, create_game


def init_games_controller(api, app):

    init_service(app)

    #game_model = get_game_model(api)
    class GameList(Resource):
        """A resource controller for a collection of games"""
        @jwt_required
        def get(self):
            return get_games()

        @jwt_required
        def post(self):
            data = request.get_json()
            identity = get_jwt_identity()
            game_id = create_game(data, identity['user_id'])
            return {'id': game_id}, 201

    class Game(Resource):
        """A resource controller for a game """
        @jwt_required
        def get(self, game_id):
            game = get_game_by_id(game_id)
            if game is not None:
                return game, 200
            api.abort(504, "Game {} doesn't exist".format(game_id))

        @jwt_required
        def delete(self, game_id):
            identity = get_jwt_identity()
            deleted = remove_game(game_id, identity['user_id'])
            return None, 204 if deleted > 0 else 404

        #@api.expect(game_model)
        @jwt_required
        def put(self, game_id):
            identity = get_jwt_identity()
            game = request.get_json()
            updated = update_game(game_id, game, identity['user_id'])
            return '', 200 if updated > 0 else 404

    api.add_resource(GameList, '/games')
    api.add_resource(Game, '/games/<string:game_id>')
