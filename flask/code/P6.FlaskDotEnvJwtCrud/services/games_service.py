from persistence.db import init_db
from persistence.games_dao import get_all_games, get_game, remove_game, update_game, add_game

def __to_game_with_likes_count__(game):
    game['likes_count'] = len(game['liked_by'])
    del game['liked_by']
    return game

def init_service(app):
    init_db(app)

def get_games():
    return [__to_game_with_likes_count__(x) for x in get_all_games()]

def get_game_by_id(game_id):
    game = get_game(game_id)
    return  __to_game_with_likes_count__(game) if game is not None else None

def delete_game(game_id, user_id):
    return remove_game(game_id, user_id)

def update_game_by_id(game_id, game, user_id):
    return update_game(game_id, game, user_id)

def create_game(game, user_id):
    return add_game(game, user_id)
