import random
from config import TOTAL_ROUNDS


games = {}


def start_round(chat_id, players):

    if chat_id not in games:

        games[chat_id] = {
            "round": 1,
            "players": players
        }

    return games[chat_id]


def next_round(chat_id):

    game = games.get(chat_id)

    if not game:
        return None

    game["round"] += 1

    if game["round"] > TOTAL_ROUNDS:
        return "finished"

    return game["round"]


def random_roles(players):

    roles = ["raja", "wazir", "chor", "sipahi"]

    random.shuffle(players)

    return dict(zip(roles, players))
