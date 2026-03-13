from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client.raja_game

users = db.users
leaderboard = db.leaderboard
