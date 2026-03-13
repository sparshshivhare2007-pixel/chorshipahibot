from telegram import Update
from telegram.ext import ContextTypes

from database.users import get_top


async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):

    top = get_top()

    text = "🏆 Leaderboard\n\n"

    rank = 1

    for user in top:

        text += f"{rank}. {user['name']} - {user['points']} pts\n"

        rank += 1

    await update.message.reply_text(text)
