from config import MAX_PLAYERS

lobbies = {}


def create_lobby(chat_id):

    lobbies[chat_id] = []


def join_lobby(chat_id, user):

    players = lobbies.get(chat_id)

    if not players:
        return "no_game"

    if user in players:
        return "already"

    if len(players) >= MAX_PLAYERS:
        return "full"

    players.append(user)

    return "joined"
