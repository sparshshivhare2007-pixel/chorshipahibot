import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

MAX_PLAYERS = 4
TOTAL_ROUNDS = 20
RAJA_POINTS = 1000
