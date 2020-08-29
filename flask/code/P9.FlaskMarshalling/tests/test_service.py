import unittest

import uuid

from flask import Flask

from services.games_service import add_game, get_games, init_service

APP = Flask("test")
APP.config['MONGO_URI'] = 'mongodb://test:test@localhost:27017/testgamestore?authSource=testgamestore'


class ServiceTests(unittest.TestCase):

     # executed prior to each test
    def setUp(self):
        init_service(APP)

    # executed after each test
    def tearDown(self):
        pass

    def test_can_create_game(self):
        unique_user = str(uuid.uuid1())
        game = add_game({'name': unique_user, 'genre': 'ARCADE', 'platforms': ['IO', 'PS4']})
        self.assertIsNotNone(game)

    def test_can_read_games_all_fields(self):
        unique_user = str(uuid.uuid1())
        add_game({'name': unique_user, 'genre': 'ARCADE', 'platforms': ['IO', 'PS4']})
        
        games, _, _, _ = get_games({}, None, 0, 10000)
        self.assertIsNotNone(games)

    def test_can_read_games_all_fields_paginated(self):
        for _ in range(0, 100):
            unique_user = str(uuid.uuid1())
            add_game({'name': unique_user, 'genre': 'ARCADE', 'platforms': ['IO', 'PS4']})
        
        for i in range(0, 10):
           games, _, _, _ = get_games({}, None, i, 10)
           self.assertTrue(len(games) == 10)
           
    def test_can_read_games_all_fields_paginated_sanitization(self):
        for _ in range(0, 100):
            unique_user = str(uuid.uuid1())
            add_game({'name': unique_user, 'genre': 'ARCADE', 'platforms': ['IO', 'PS4']})
        
        for _ in range(0, 10):
           games, _, sanitized_page, sanitized_limit = get_games({}, None, -1, -1)
           self.assertTrue(len(games) == 10)
           self.assertTrue(sanitized_page == 1)
           self.assertTrue(sanitized_limit == 10)
         
if __name__ == '__main__':
    unittest.main()