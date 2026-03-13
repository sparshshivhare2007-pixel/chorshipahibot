from telegram import Update
from telegram.ext import ContextTypes
from database.mongo import users


async def transferpoints(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) < 3:
        await update.message.reply_text(
            "Usage: /transferpoints from_id to_id points"
        )
        return

    from_id = int(context.args[0])
    to_id = int(context.args[1])
    points = int(context.args[2])

    users.update_one(
        {"_id": from_id},
        {"$inc": {"points": -points}}
    )

    users.update_one(
        {"_id": to_id},
        {"$inc": {"points": points}}
    )

    await update.message.reply_text(
        f"Transferred {points} points"
    )
