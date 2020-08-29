import unittest

import uuid

from app import get_app

from persistence.db import init_db

from persistence.games_dao import create_db_game

from flask import json

class ApiTests(unittest.TestCase):

     # executed prior to each test
    def setUp(self):
        app = get_app("test", {'MONGO_URI' : 'mongodb://test:test@localhost:27017/testgamestore?authSource=testgamestore'})
        app.testing = True
        #APP.config[
        init_db(app)
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    def test_get_games_from_api(self):
        result = self.app.get('/games')
        self.assertIsNotNone(result)

    def test_get_games_paginated_from_api(self):
        result = self.app.get('/games?page=1&limit=2')
        response = json.loads(result.data)
        # print(response)
        self.assertLessEqual(len(response['data']), 2)
    
    def test_get_games_fields_projection(self):
        result = self.app.get('/games?fields=name,genre')
        response = json.loads(result.data)
        self.assertIsNotNone(response)

    
    def test_get_games_search(self):
        unique_id = str(uuid.uuid1())

        for i in range(0, 5):
            game_name = f'{unique_id}_{i}'
            print(game_name)
            create_db_game({'name': game_name, 'genre': 'Arcade', 'platforms': ['PS4']})

        result = self.app.get('/games?search=' + unique_id)
        response = json.loads(result.data)
        # print(response)
        self.assertLessEqual(len(response['data']), 5)

         
if __name__ == '__main__':
    unittest.main()