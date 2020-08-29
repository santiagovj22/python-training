#Example 15
from flask import Flask, jsonify
from flask_restx import Api
from logging import Logger
from werkzeug.exceptions import HTTPException

import logging.config
from common.app_exceptions import AppException
from controllers.games_controller import init_games_controller

logging.config.fileConfig('./logging.ini')
LOG = logging.getLogger('App Logger')

app = Flask(__name__)

api = Api(app, validate=True)

init_games_controller(api)

@api.errorhandler(AppException)
def handle_api_errors(error):
    LOG.error('Error ID %s', error.log_id)
    LOG.error(error, stack_info=True)
    detail = error.to_dict()

    return  {'error': detail} , error.status_code

app.run(debug=False)



#LandmarksComment.js
