from flask_restx import fields, Api

def get_credentials_model(api: Api):
    return api.model('Credentials', {
        'login': fields.String(required=True),
        'password': fields.String(required=True),
    })
