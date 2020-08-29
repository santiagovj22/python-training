import logging

from persistence.db import get_games_collection

LOG = logging.getLogger('Games Dao')

def create_db_game(game):
    LOG.debug('Create game %s', game)
    game_id = str(get_games_collection().insert_one(game))
    return game_id

def get_db_games(game_fields, search_term, skip, limit):
    LOG.debug('fields = %s', game_fields)
    LOG.debug('search = %s', search_term)
    LOG.debug('pagination skip= %s limit=%s', skip, limit)

    query = {}

    if search_term:
        query = {'name':  {'$regex': search_term}}
    
    # Get Number of total Rows
    rows = get_games_collection().count_documents(query)

    if len(game_fields) == 0:
        return [row for row in get_games_collection().find(query).sort('name').skip(skip).limit(limit)], rows

    projected_fields = {key:1 for key in game_fields}
    return [row for row in get_games_collection().find(query, projected_fields).sort('name').skip(skip).limit(limit)], rows

