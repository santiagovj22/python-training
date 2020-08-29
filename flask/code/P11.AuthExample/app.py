
from flask import Flask, render_template, jsonify

from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, get_raw_jwt

from flask_dotenv import DotEnv

from services.users_service import update_user

app = Flask(__name__)

#get configuration from .env
env = DotEnv()
env.init_app(app, verbose_mode=True)
app.config['JWT_PUBLIC_KEY'] = open('pubkey.pem').read()
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

@app.route("/api/v1/auth", methods=['POST'])
@jwt_required
def auth_user():
    identity = get_raw_jwt()
    user_data = update_user(identity['email'])
    return jsonify({'User': user_data, 'JWT' : identity})

if __name__ == "__main__":
    app.run()
