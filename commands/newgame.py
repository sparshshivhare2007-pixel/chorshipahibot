from telegram import Update
from telegram.ext import ContextTypes

from game.lobby import lobbies
from game.roles import assign_roles


async def newgame(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    players = lobbies.get(chat_id)

    if not players or len(players) < 4:

        await update.message.reply_text("Need 4 players to start.")
        return

    roles = assign_roles(players)

    raja = roles["raja"]
    wazir = roles["wazir"]

    text = f"👑 Raja is {raja['name']}\n\nWazir choose Chor and Sipahi"

    await update.message.reply_text(text)

    context.chat_data["roles"] = roles
