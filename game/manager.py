import random

games = {}

roles = ["raja", "wazir", "chor", "sipahi"]

def create_game(chat_id):
    games[chat_id] = {
        "players": [],
        "roles": {},
        "points": {},
        "round": 0
    }

def add_player(chat_id, user):
    if user not in games[chat_id]["players"]:
        games[chat_id]["players"].append(user)
        games[chat_id]["points"][user.id] = 0

def assign_roles(chat_id):
    players = games[chat_id]["players"]
    random.shuffle(players)

    role_map = {}

    for i, role in enumerate(roles):
        role_map[role] = players[i]

    games[chat_id]["roles"] = role_map

    return role_map
