from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.likes_service import init_service, get_likes, add_likes, remove_likes

def init_likes_controller(api, app):

    init_service(app)

    #game_model = get_game_model(api)
    class UserLikesList(Resource):
        """A resource controller for the likes from users on a game"""
        @jwt_required
        def get(self, game_id):
            return get_likes(game_id)

        @jwt_required
        def post(self, game_id):
            identity = get_jwt_identity()
            return add_likes(game_id, identity['user_id'])

        @jwt_required
        def delete(self, game_id):
            identity = get_jwt_identity()
            return remove_likes(game_id, identity['user_id'])      

    api.add_resource(UserLikesList, '/games/<string:game_id>/likes')
