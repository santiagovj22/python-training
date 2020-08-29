
from flask import Flask, render_template, jsonify, request

from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, get_raw_jwt, create_access_token

from flask_dotenv import DotEnv

from services.users_service import update_user, get_user

from services.auth_service import verify_user, sign_api_token

app = Flask(__name__)

#get configuration from .env
env = DotEnv()
env.init_app(app, verbose_mode=True)
PUBLIC_KEY = open('pubkey.pem').read()
app.config['JWT_PUBLIC_KEY'] = PUBLIC_KEY
app.config['JWT_IDENTITY_CLAIM'] = 'jti'


jwt = JWTManager(app)

@app.route("/")
def main():
    return render_template('home.html')

@app.route("/auth")
def auth():    
    return render_template('auth.html')

@app.route("/logout")
def logout():
    return render_template('logout.html')    

@app.route("/api/v1/authLogin", methods=['POST'])
def auth_login_user():
    args = request.args
    code = args['code']

    print(f'Code received is {code}')
    user, jwt_token = verify_user(code, PUBLIC_KEY)
   
    user_info = update_user(user)

    # .. you can also create your own JWT and use the original JWT's info.
    #jwt_token = sign_api_token(user)

    user_response = {'user_info':user_info, 'jwt':jwt_token}
    return jsonify(user_response)

@app.route("/api/v1/userInfo", methods=['GET'])
@jwt_required
def who_i_am():
    identity = get_raw_jwt()
    return  get_user(identity['email'])

if __name__ == "__main__":
    app.run()
