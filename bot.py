from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from config import BOT_TOKEN

from commands.startgame import startgame
from commands.join import join
from commands.newgame import newgame
from commands.endgame import endgame
from commands.leaderboard import leaderboard

from game.rounds import wazir_choice, raja_guess

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("startgame", startgame))
app.add_handler(CommandHandler("join", join))
app.add_handler(CommandHandler("newgame", newgame))
app.add_handler(CommandHandler("endgame", endgame))
app.add_handler(CommandHandler("leaderboard", leaderboard))

app.add_handler(CallbackQueryHandler(wazir_choice, pattern="wazir_"))
app.add_handler(CallbackQueryHandler(raja_guess, pattern="guess_"))

app.run_polling()
