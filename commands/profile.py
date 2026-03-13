from telegram import Update
from telegram.ext import ContextTypes

from database.mongo import users


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    user = users.find_one({"_id": user_id})

    if not user:
        return

    text = f"""
Profile

Raja: {user['raja']}
Wazir: {user['wazir']}
Chor: {user['chor']}
Sipahi: {user['sipahi']}

Total Points: {user['points']}
"""

    await update.message.reply_text(text)
