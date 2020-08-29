import uuid

from flask import request

from flask_restx import Resource, fields, marshal

GAMES = [{'_id': 'game1', 'name': 'Mario', 'author_id': 'JROCA', 'author': 'Javier',
          'genre': "Arcade", 'platforms': ["IO"], 'xtra':'ABC', 'pwd': 'pwd2'},
         {'_id': 'game2', 'name': 'Crash Team Racing', 'author_id': 'CVARGAS', 'author': 'Carlos',
          'genre': "Arcade", 'platforms': ["PSP", "PS4"], 'xtra': 'XYZ', 'pwd': 'pwd2'}
        ]

def init_games_controller(api):

    game_short_model = api.model('Game ', {'id': fields.String(attribute='_id'),
                                           'name': fields.String, 'genre': fields.String,
                                           'platforms': fields.List(fields.String)})

    game_input_model = api.model('Game Input', {'name': fields.String(required=True),
                                                'genre': fields.String(required=True),
                                                'platforms': fields.List(fields.String(), required=True)})

    class GameList(Resource):
        """A resource controller for a collection of games"""

        @api.marshal_with(game_short_model, skip_none=True)
        def get(self):
            return GAMES

        @api.expect(game_input_model)
        def post(self):
            game = request.get_json()
            game = marshal(game, game_input_model)
            game['_id'] = str(uuid.uuid1())
            GAMES.append(game)
            return {'id': game['_id']}

    api.add_resource(GameList, '/games')
