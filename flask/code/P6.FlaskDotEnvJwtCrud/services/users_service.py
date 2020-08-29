from hashlib import md5

from persistence.users_dao import get_all_users, add_user, get_user_by_credentials
from persistence.db import init_db

def init_service(app):
    init_db(app)

def get_users():
    return get_all_users()

def create_user(user):
    #set password to it's md5 hash
    md5_password = md5(user['password'].encode()).hexdigest()
    user['password'] = md5_password
    return add_user(user)
