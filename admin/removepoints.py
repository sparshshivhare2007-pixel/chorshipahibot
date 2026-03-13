from telegram import Update
from telegram.ext import ContextTypes
from database.mongo import users


async def removepoints(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) < 2:
        await update.message.reply_text(
            "Usage: /removepoints user_id points"
        )
        return

    user_id = int(context.args[0])
    points = int(context.args[1])

    users.update_one(
        {"_id": user_id},
        {"$inc": {"points": -points}}
    )

    await update.message.reply_text(
        f"Removed {points} points from {user_id}"
    )
