from telegram import Update
from telegram.ext import ContextTypes
from game.manager import games

async def endgame(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    if chat_id not in games:
        return

    points = games[chat_id]["points"]

    text = "🏆 Game Over\n\nScores:\n"

    for user, pts in points.items():
        text += f"{user} : {pts}\n"

    await update.message.reply_text(text)

    del games[chat_id]
