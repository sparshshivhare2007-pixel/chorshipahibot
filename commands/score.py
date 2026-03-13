from telegram import Update
from telegram.ext import ContextTypes

from database.users import get_points


async def score(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    pts = get_points(user_id)

    await update.message.reply_text(
        f"Your points: {pts}"
    )
