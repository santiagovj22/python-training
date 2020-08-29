import logging

from persistence.db import init_db
from persistence.games_dao import get_db_games, create_db_game

LOG = logging.getLogger('Games Service')

def init_service(app):
    LOG.info('Starting Games Service')
    init_db(app)

def get_games(game_fields, search_term, page, limit):
    sanitized_page, sanitized_limit = __sanitize_pagination__(page, limit)
    skip = (sanitized_page - 1) * sanitized_limit
    data, rows = get_db_games(__sanitize_fields__(game_fields, {'_id', 'genre', 'name', 'platforms'}),
                              search_term, skip, sanitized_limit)
    # Number of Pages
    return data, rows, sanitized_page, sanitized_limit

def add_game(game):
    # dont' forget to sanitize game!
    return create_db_game(game)

def __sanitize_fields__(games_fields, all_fields):
    allowed_fields = set(games_fields).intersection(all_fields)
    LOG.debug('sanitized_fields = %s', allowed_fields)
    return list(allowed_fields)

def __sanitize_pagination__(page, limit):
    if limit < 1 or limit > 10:
        limit = 10
    if page < 1:
        page = 1
    return page, limit
