import random


def assign_roles(players):

    roles = ["raja", "wazir", "chor", "sipahi"]

    random.shuffle(players)

    data = {}

    for i, role in enumerate(roles):

        data[role] = players[i]

    return data
