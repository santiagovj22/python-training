from typing import List

from persistence.db_models import Games
from persistence.db import to_object_id

def get_all_games()->List[Games]:
    print(len(Games.objects()))
    return [x.as_dict() for x in Games.objects()]

def get_game(_id):
    print(_id)
    game = Games.objects.get(id=to_object_id(_id))
    if game is not None:
        return game.as_dict()
    return None

def add_game(game, user_id):
    game['created_by'] = user_id
    new_game = Games(**game).save()
    return str(new_game.id)

def remove_game(_id, user_id):
    game = Games.objects.get(id=to_object_id(_id))
    if game['created_by'] == user_id:
        game.delete()
        return 1
    raise('Invalid user')

def update_game(_id, game, user_id):
    old_game = Games.objects.get(id=to_object_id(_id))
    if old_game['created_by'] == user_id:
        game.update(**game)
        return 1
    raise('Invalid user')

def add_like_to_game(game_id, user_id):
    Games.objects.get(id=to_object_id(game_id)).update(push__liked_by=user_id)

def remove_like_to_game(game_id, user_id):
    Games.objects.get(id=to_object_id(game_id)).update(pull__liked_by=user_id)
