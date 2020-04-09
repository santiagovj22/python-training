import uuid

GAMES = {}

def get_games():
    return [row for row in GAMES.values()]

def get_game(game_id):
    return GAMES[game_id] if (game_id in GAMES) else None

def delete_game(game_id):
    if game_id in GAMES:
        del GAMES[game_id]
        return 1
    return 0

def update_game(game_id, game):
    if game_id in GAMES:
        game['id'] = game_id
        GAMES[game_id] = game
        return 1
    return 0

def add_game(game):
    game_id = str(uuid.uuid1())
    game['id'] = game_id
    GAMES[game_id] = game
    return game_id
