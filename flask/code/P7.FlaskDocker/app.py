#Minimal App
from flask import Flask

app = Flask(__name__)

@app.route('/tours')
def main():
    return "Hello from Traveler!", 200

#app.run()
