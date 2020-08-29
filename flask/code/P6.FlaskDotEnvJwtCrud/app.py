
#Example 6
from flask import Flask
from flask_dotenv import DotEnv
from flask_restx import Api
from flask_jwt_extended import JWTManager

from controllers.auth_controller import init_auth_controller
from controllers.games_controller import init_games_controller
from controllers.likes_controller import init_likes_controller
from controllers.users_controller import init_users_controller

#create the flask app
app = Flask(__name__)

#get configuration from .env
env = DotEnv()
env.init_app(app, verbose_mode=True)

#Configure DB
MONGO_CNX = 'mongodb://flask:flaskpwd@localhost:27017/gamestore?authSource=gamestore'
app.config['MONGODB_SETTINGS'] = {'host': MONGO_CNX}

#create api
api = Api(app, validate=False)

#configure jwt
jwt = JWTManager(app)

#init api controllers
init_auth_controller(api, app)
init_games_controller(api, app)
init_likes_controller(api, app)
init_users_controller(api, app)

#run app
app.run(debug=False)
