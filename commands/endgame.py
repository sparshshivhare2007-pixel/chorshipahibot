from telegram import Update
from telegram.ext import ContextTypes

from game.lobby import lobbies


async def endgame(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    if chat_id in lobbies:
        del lobbies[chat_id]

    await update.message.reply_text("Game ended.")
