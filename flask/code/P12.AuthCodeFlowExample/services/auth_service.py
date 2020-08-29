import http.client

import json

import jwt

import datetime

from flask_jwt_extended import create_access_token

def sign_api_token(user):
    expiry_on = datetime.timedelta(days=1)
    jwt_token = create_access_token(identity={'user_id': user, 'nickname': 'parce'}, expires_delta=expiry_on)
    return jwt_token

def _get_id_token(auth_code):
    conn = http.client.HTTPSConnection("ixjala.auth0.com")
    auth_url = '/oauth/token'
    client_id = 'sJXY8ISV8FMuADxUQelw4WO2rEgP8ELM'
    #client_secret = 'MDj8EOHOeWBeClBSdeMOK5yW1IkyUuyr8MCd5dD-bnE5MeEn1Z-uNMceiRuhd7c0'
    redirect_uri = 'http://localhost:5000/auth'
    #payload = f'grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&code={auth_code}&redirect_uri={redirect_uri}'

    payload = f'grant_type=authorization_code&client_id={client_id}&code={auth_code}&redirect_uri={redirect_uri}'


    headers = { 'content-type': 'application/x-www-form-urlencoded' }

    print(f'URI = {auth_url} and payload is {payload}')    

    conn.request('POST', auth_url, payload, headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode('utf-8'))

    return json.loads(data.decode('utf-8'))

def verify_user(auth_code, public_key):
    id_token = _get_id_token(auth_code)['id_token']
    decoded = jwt.decode(id_token, public_key, algorithms='RS256', verify=False, 
                         options={'JWT_DECODE_AUDIENCE' : 'sJXY8ISV8FMuADxUQelw4WO2rEgP8ELM', 'JWT_IDENTITY_CLAIM' : 'jti'} )
    return decoded['email'], id_token

