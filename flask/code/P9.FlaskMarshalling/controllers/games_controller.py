import logging

from flask import request

from flask_restx import Resource, fields, marshal, reqparse

from services.games_service import init_service, get_games, add_game

LOG = logging.getLogger('Games Controller')

def init_games_controller(app, api):

    LOG.debug('Starting Games Controller')

    game_model = api.model('Game ', {'_id': fields.String(), 'name': fields.String,
                                     'genre': fields.String, 'platforms': fields.List(fields.String)})

    game_input_model = api.model('Game Input', {'name': fields.String(required=True), 'genre': fields.String(required=True), 'platforms': fields.List(fields.String(), requried=True)})

    init_service(app)

    class GameList(Resource):
        """A resource controller for a collection of games"""

        def get(self):
            LOG.debug('Called from the web')
            parser = reqparse.RequestParser()
            fields_arg, search_arg, limit_arg, page_arg = self.parse_query(parser)

            LOG.debug('Fields: %s Search: %s Page: %s Limit: %s', fields_arg, search_arg, limit_arg, page_arg)

            games, rows, page, limit = get_games(fields_arg, search_arg, page_arg, limit_arg)

            LOG.debug('Rows: %s Page: %s Limit: %s', rows, page, limit)

            games_json = marshal(games, game_model, skip_none=True) 
            payload = {'data': games_json, 'page': page, 'limit': limit, 'rows': rows}
            
            return payload
        
        def parse_query(self, parser):
            parser.add_argument('fields', action='split')
            parser.add_argument('search')
            parser.add_argument('limit', type=int)
            parser.add_argument('page', type=int)
            args = parser.parse_args()

            fields_arg = args['fields']
            limit_arg = args['limit']
            page_arg = args['page']

            if fields_arg is None:
                fields_arg = []
            else:
                fields_arg = [field for field in fields_arg if field]

            # default
            if limit_arg is None:
                limit_arg = 2
            
            if page_arg is None:
                page_arg = 1

            return fields_arg, args['search'], limit_arg, page_arg

        @api.expect(game_input_model)
        def post(self):
            game = request.get_json()
            game = marshal(game, game_input_model)
            game_id = add_game(game)
            return {'id': game_id}, 201

    api.add_resource(GameList, '/games')
