from flask import request
from flask_restx import Resource

from controllers.input_models import get_credentials_model
from services.auth_service import authenticate_user


def init_auth_controller(api, app):

    credentials_model = get_credentials_model(api)

    class Auth(Resource):
        """A resource controller for authenticating users"""

        @api.expect(credentials_model)
        def post(self):
            data = request.get_json()
            auth_response = authenticate_user(data['login'], data['password'])
            return auth_response, 200

    api.add_resource(Auth, '/auth/login')
