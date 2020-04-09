#Example 5
from flask import Flask
from flask_restx import Api
from controllers.games_controller import init_games_controller

app = Flask(__name__)
api = Api(app, validate=True)

init_games_controller(api)

app.run(debug=False)
