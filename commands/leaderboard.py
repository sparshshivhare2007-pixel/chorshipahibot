from telegram import Update
from telegram.ext import ContextTypes
from database.leaderboard import get_top

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):

    top = get_top()

    text = "🏆 Top 10 Players\n\n"

    for i, user in enumerate(top, 1):

        text += f"{i}. {user['name']} — {user['points']} pts\n"

    await update.message.reply_text(text)
