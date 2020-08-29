USERS = {}

def update_user(user):
    if user not in USERS:
        USERS[user] = 0
    USERS[user] += 1
    return {'name': user, 'access': USERS[user]}

