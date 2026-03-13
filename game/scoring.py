from database.users import add_points
from config import RAJA_POINTS


def round_score(roles, guess_correct):

    raja = roles["raja"]
    wazir = roles["wazir"]
    chor = roles["chor"]
    sipahi = roles["sipahi"]

    add_points(raja["id"], RAJA_POINTS)

    wazir_points = 500
    sipahi_points = 300

    if guess_correct:

        add_points(wazir["id"], wazir_points)
        add_points(sipahi["id"], sipahi_points)

    else:

        add_points(chor["id"], wazir_points)
