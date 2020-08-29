from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from services.users_service import init_service, get_users, create_user


def init_users_controller(api, app):

    init_service(app)

    #game_model = get_game_model(api)
    class UsersList(Resource):
        """A resource controller for the users"""
        @jwt_required
        def get(self):
            return get_users()

        def post(self):
            user = request.get_json()
            print(user)
            user_id = create_user(user)
            return {'id':user_id}, 201

    api.add_resource(UsersList, '/users')
