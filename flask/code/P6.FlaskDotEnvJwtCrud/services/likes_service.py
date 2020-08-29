from persistence.db import init_db
from persistence.games_dao import get_game, add_like_to_game, remove_like_to_game
from persistence.users_dao import get_users_by_ids

def init_service(app):
    init_db(app)

def get_likes(game_id):
    game = get_game(game_id)
    likes = get_users_by_ids(game['liked_by'])
    return likes

def add_likes(game_id, user_id):
    add_like_to_game(game_id, user_id)

def remove_likes(game_id, user_id):
    remove_like_to_game(game_id, user_id)
