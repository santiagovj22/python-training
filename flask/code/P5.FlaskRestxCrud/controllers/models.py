from flask_restx import fields, Api

def get_game_model(api: Api):
    return api.model('Game', {
        'id': fields.String(readonly=True),
        'name': fields.String(required=True),
        'genre': fields.String(required=True),
        'platforms': fields.List(fields.String(), required=True)
    })
