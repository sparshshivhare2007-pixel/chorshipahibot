import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

MAX_PLAYERS = 4
TOTAL_ROUNDS = 10

POINTS = {
    "correct_guess": 1000,
    "wrong_guess": 500
}
