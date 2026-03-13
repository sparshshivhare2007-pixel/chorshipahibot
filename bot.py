import logging

from telegram.ext import (
    Application,
    CommandHandler,
)

from config import BOT_TOKEN

# command imports
from commands.startgame import startgame
from commands.newgame import newgame
from commands.endgame import endgame
from commands.leaderboard import leaderboard
from commands.score import score
from commands.profile import profile

# admin commands
from admin.addpoints import addpoints
from admin.removepoints import removepoints
from admin.transferpoints import transferpoints


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    # game commands
    app.add_handler(CommandHandler("startgame", startgame))
    app.add_handler(CommandHandler("newgame", newgame))
    app.add_handler(CommandHandler("endgame", endgame))

    # user commands
    app.add_handler(CommandHandler("leaderboard", leaderboard))
    app.add_handler(CommandHandler("score", score))
    app.add_handler(CommandHandler("profile", profile))

    # admin commands
    app.add_handler(CommandHandler("addpoints", addpoints))
    app.add_handler(CommandHandler("removepoints", removepoints))
    app.add_handler(CommandHandler("transferpoints", transferpoints))

    print("Bot started successfully")

    app.run_polling()


if __name__ == "__main__":
    main()
