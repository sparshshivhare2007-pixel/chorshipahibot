from telegram import Update
from telegram.ext import ContextTypes
from game.manager import create_game

async def startgame(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    create_game(chat_id)

    await update.message.reply_text(
        "🎮 Raja Wazir Chor Sipahi Game Started!\n\n"
        "Players join with /join\n"
        "Need 4 players."
    )
