from flask_pymongo import PyMongo

class DatabaseConnection:
    ready = False
    connection = PyMongo()
    def init_db(self, app):
        if not self.ready:
            self.ready = True
            self.connection.init_app(app)
    def get_collection(self, name):
        return self.connection.db.get_collection(name)