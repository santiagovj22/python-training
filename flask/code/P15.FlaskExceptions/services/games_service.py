import uuid

import logging

from common.app_exceptions import NotFoundException, AppException

GAMES = {}

LOG = logging.getLogger('Service')

def get_games():
    return [row for row in GAMES.values()]

def get_game(game_id):
    return GAMES[game_id] if (game_id in GAMES) else None

def delete_game(game_id):
    LOG.debug('Game_id is %s', game_id)
    if game_id in GAMES:
        del GAMES[game_id]
        return 1
    raise NotFoundException('Game was not found. Cannot delete')

def update_game(game_id, game):
    if game_id in GAMES:
        game['id'] = game_id
        GAMES[game_id] = game
        return 1
    raise AppException('Game was not found. Cannot update',
payload = {'errors': {'game_id': 'Not an guid', 'name': 'Already exists'}})


def add_game(game):
    game_id = str(uuid.uuid1())
    game['id'] = game_id
    GAMES[game_id] = game
    return game_id
