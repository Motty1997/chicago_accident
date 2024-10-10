from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
chicago_accidents_db = client['chicago_accidents']

daily = chicago_accidents_db['daily']
weekly = chicago_accidents_db['weekly']
monthly = chicago_accidents_db['monthly']
