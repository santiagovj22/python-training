import uuid

def get_service():
    games = {}

    def get_all_games():
        return [row for row in games.values()]

    def get_game(_id):
        return games[_id] if (_id in games) else None

    def delete_game(_id):
        if id in games:
            del games[_id]
            return 1
        return 0

    def update_game(_id, game):
        if _id in games:
            games[_id] = game
            return 1
        return 0

    def insert_game(game):
        _id = str(uuid.uuid1())
        game['id'] = _id
        games[_id] = game
        return _id

    return get_all_games, get_game, delete_game, update_game, insert_game
