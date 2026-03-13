from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

from game.lobby import create_lobby


async def startgame(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    create_lobby(chat_id)

    keyboard = [
        [InlineKeyboardButton("Join Game", callback_data="join")]
    ]

    await update.message.reply_text(
        "🎮 Raja Wazir Chor Sipahi\n\n"
        "Press Join to join the game\n"
        "Players: 0/4",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
