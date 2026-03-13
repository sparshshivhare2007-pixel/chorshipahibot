from telegram import Update
from telegram.ext import ContextTypes
from game.manager import games, add_player

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
    user = update.effective_user

    if chat_id not in games:
        await update.message.reply_text("Start game first using /startgame")
        return

    add_player(chat_id, user)

    players = games[chat_id]["players"]

    await update.message.reply_text(
        f"{user.first_name} joined!\nPlayers: {len(players)}/4"
    )
