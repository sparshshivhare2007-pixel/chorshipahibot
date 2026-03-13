from database.mongo import users


def add_user(user_id, name):

    if not users.find_one({"_id": user_id}):

        users.insert_one({
            "_id": user_id,
            "name": name,
            "points": 0,
            "raja": 0,
            "wazir": 0,
            "chor": 0,
            "sipahi": 0
        })


def add_points(user_id, points):

    users.update_one(
        {"_id": user_id},
        {"$inc": {"points": points}}
    )


def get_points(user_id):

    user = users.find_one({"_id": user_id})

    if user:
        return user["points"]

    return 0


def get_top():

    return users.find().sort("points", -1).limit(10)
