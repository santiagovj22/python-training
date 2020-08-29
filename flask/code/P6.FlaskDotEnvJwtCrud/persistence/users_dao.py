from typing import List
from mongoengine.queryset.visitor import Q

from persistence.db_models import Users

def get_all_users()->List[Users]:
    return [x.as_dict() for  x in Users.objects().only('id', 'name')]

def add_user(user):
    new_user = Users(**user).save()
    return str(new_user.id)

def get_users_by_ids(user_ids)->List[Users]:
    if len(user_ids) > 0:
        return [x.as_dict() for x in Users.objects(id__in=user_ids)]
    return []
    #.only('_id', 'name')

def get_user_by_credentials(name, pwd):
    return Users.objects(Q(name=name) & Q(password=pwd)).first().as_dict()
