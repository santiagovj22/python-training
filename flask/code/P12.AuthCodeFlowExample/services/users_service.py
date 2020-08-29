from datetime import date

import random

USERS = {}

def update_user(user):
    if user not in USERS:
        USERS[user] = {'count':  0, 'creationDate': f'{date.today()}'}
    USERS[user]['count'] += 1
    return {'name': user, 'access': USERS[user]['count']}

def get_user(user):
    db_user = USERS[user]
    return {'name': user, 'data': { 'access:' : db_user['count'], 'creationDate': db_user['creationDate'], 'tours': random.randint(10, 80)}}
