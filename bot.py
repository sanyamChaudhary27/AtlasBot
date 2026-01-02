import os
import telebot
from ai_engine import get_response

BOT_TOKEN = os.environ("TELEGRAM_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=labda m: True)
def handle_message(message):
   user_id = message.from_user.id
   user_text = message.text
   history = get_history(user_id)
   response = get_response(user_text, history)
   save_message(user_id, user_text, "user")
   save_message(user_id, response, "model")

   bot.reply_to(message, response)

def start_bot():
    print("Atlas (Split-File Version) is Online...")
    bot.infinity_polling()