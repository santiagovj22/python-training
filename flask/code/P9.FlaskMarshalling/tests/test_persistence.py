import unittest

import uuid

from flask import Flask

from persistence.db import init_db

from persistence.games_dao import create_db_game, get_db_games

APP = Flask("test")
APP.config['MONGO_URI'] = 'mongodb://test:test@localhost:27017/testgamestore?authSource=testgamestore'

class PersistenceTests(unittest.TestCase):

     # executed prior to each test
    def setUp(self):
        # print('\nSetup')
        init_db(APP)

    # executed after each test
    def tearDown(self):
        # print('\nTear Down')
        pass

    def test_can_create_game_on_db(self):
        unique_user = str(uuid.uuid1())
        game = create_db_game({'name': unique_user, 'genre': 'ARCADE', 'platforms': ['IO', 'PS4']})
        self.assertIsNotNone(game)

    def test_can_read_games_from_db(self):
        games, _ = get_db_games({}, None, 0, 10000)
        self.assertIsNotNone(games)
       
    def test_can_add_games_to_db(self):
        _, rows_before = get_db_games({}, None, 0, 10000)

        for _ in range(0, 100):
            unique_user = str(uuid.uuid1())
            create_db_game({'name': unique_user, 'genre': 'ARCADE', 'platforms': ['IO', 'PS4']})
        
        _, rows_after = get_db_games({}, None, 0, 10000)
        
        self.assertLess(rows_before, rows_after)
        self.assertEqual(rows_before + 100, rows_after)



if __name__ == '__main__':
    unittest.main()