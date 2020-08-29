import datetime
from hashlib import md5

from flask_jwt_extended import create_access_token

from persistence.db import init_db
from persistence.users_dao import  get_user_by_credentials

def init_service(app):
    init_db(app)

def authenticate_user(login, pwd):
    try:
        md5_password = md5(pwd.encode()).hexdigest()
        user = get_user_by_credentials(login, md5_password)
        expiry_on = datetime.timedelta(days=1)
        access_token = create_access_token(identity={'user_id': user['id'],
                                                     'name': user['name']}, expires_delta=expiry_on)
        return {'access_token': access_token, 'user_id': user['id'], 'user_name': user['name']}
    except:
        raise Exception("Invalid User")
