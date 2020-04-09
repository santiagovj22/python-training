from pymongo import MongoClient
       
def get_games_db(host, login, pwd):
    client = MongoClient(f'mongodb://{login}:{pwd}@{host}/?authSource=gamestore')
    return client.get_database('gamestore').get_collection('games')