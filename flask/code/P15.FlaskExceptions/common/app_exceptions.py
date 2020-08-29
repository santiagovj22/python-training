from flask import jsonify
from uuid import uuid1

class AppException(Exception):
    status_code = 400
    log_id = None

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message

        self.log_id = f'{uuid1()}'

        if status_code is not None:
            self.status_code = status_code

        self.payload = payload

    def to_dict(self):
        payload = dict(self.payload or ())
        payload['message'] = self.message
        payload['code'] = self.status_code
        payload['logRef'] = self.log_id
        return payload

class NotFoundException(AppException):
    def __init__(self, message):
        AppException.__init__(self, message, 404)
