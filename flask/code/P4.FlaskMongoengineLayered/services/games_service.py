from persistence.db import init_db, get_all, get_one, remove, add, update

def get_service(app):

    init_db(app)

    def __to_game__(game_row):
        return {'id': str(game_row.id), 'name': game_row.name,
                'genre': game_row.genre, 'platforms': game_row.platforms}

    def get_all_games():
        return  [__to_game__(x) for x in get_all()]

    def get_game(_id):
        return __to_game__(get_one(_id))

    def delete_game(_id):
        return remove(_id)

    def update_game(_id, game):
        if 'id' in game:
            del game['id']
        return update(_id, game)

    def insert_game(game):
        if 'id' in game:
            del game['id']
        return add(game)

    return get_all_games, get_game, delete_game, update_game, insert_game
