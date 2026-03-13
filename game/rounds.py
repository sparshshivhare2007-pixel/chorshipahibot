from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from game.manager import games
from config import POINTS

async def wazir_choice(update, context):

    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat.id
    chosen_id = int(query.data.split("_")[1])

    games[chat_id]["raja"] = chosen_id

    await query.edit_message_text("Wazir selected Raja!")

async def raja_guess(update, context):

    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat.id

    guess_id = int(query.data.split("_")[1])
    chor = games[chat_id]["roles"]["chor"]

    if guess_id == chor.id:

        games[chat_id]["points"][guess_id] += POINTS["correct_guess"]

        await query.edit_message_text("Correct Guess! Raja Wins.")

    else:

        games[chat_id]["points"][guess_id] += POINTS["wrong_guess"]

        await query.edit_message_text("Wrong Guess!")
