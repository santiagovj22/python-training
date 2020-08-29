#Example 9

import logging

from flask import Flask
from flask_restx import Api
from controllers.games_controller import init_games_controller


def get_app(name, configuration):
    app = Flask(name)
    #Configure logger
    #LOG_FILENAME = './logs/app.log'
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    
    app.logger.debug('Starting API Server')

    app.config['MONGO_URI'] = configuration['MONGO_URI']

    api = Api(app, validate=True)

    init_games_controller(app, api)

    return app


if __name__ == '__main__':
    print('start')
    get_app(__name__, {'MONGO_URI' :'mongodb://flask:flaskpwd@localhost:27017/gamestore?authSource=gamestore'}).run(debug=False)
