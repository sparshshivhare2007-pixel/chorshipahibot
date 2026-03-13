from telegram import Update
from telegram.ext import ContextTypes
from game.manager import games, assign_roles

async def newgame(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    if len(games[chat_id]["players"]) < 4:
        await update.message.reply_text("Need 4 players to start.")
        return

    roles = assign_roles(chat_id)

    wazir = roles["wazir"]

    await update.message.reply_text(
        f"Game Started!\n\n"
        f"Wazir is {wazir.first_name}\n"
        f"Wazir choose Raja."
    )
