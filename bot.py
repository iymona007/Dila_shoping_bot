from unittest.mock import call
import random
import PIL
import telebot
import os
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
from telebot import types
from flask import Flask, request
load_dotenv()   

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__) 
user_state = {}
ID = 123456789


@bot.message_handler(commands=['start'])
def start(message):
    contact = "@USAshoPPing1997"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton("🛍 Buyurtma berish uchun kontakt")
    button2 = types.KeyboardButton("📞 Biz bilan bog'lanish")
    button3 = types.KeyboardButton("📩 telegram kanalimiz:")
    button4 = types.KeyboardButton("📸 instagram:")

    markup.add(button1, button2)
    markup.add(button3, button4)

    bot.send_message(
        message.chat.id,
        "Assalomu alaykum! Dila_shoping botiga xush kelibsiz! 💄 💅 🧴",
        reply_markup=markup
    )


    bot.send_message(
        message.chat.id,
        "🌐 Web sayt:\nhttps://dila-shoping-q1r0.onrender.com"
    )


@bot.message_handler(
    func=lambda message: message.text == "🛍 Buyurtma berish uchun kontakt"
)
def order(message):
    bot.send_message(
        message.chat.id,
        "Buyurtma berish uchun kontakt: @USAshoPPing1997"
    )


@bot.message_handler(
    func=lambda message: message.text == "📞 Biz bilan bog'lanish"
)
def contact(message):
    bot.send_message(
        message.chat.id,
        "Biz bilan bog'lanish: 909123555"
    )


@bot.message_handler(
    func=lambda message: message.text == "📩 telegram kanalimiz:"
)
def channel(message):
    bot.send_message(
        message.chat.id,
        "Telegram kanalimiz:\n"
        "https://t.me/Dil_USaAngliyaTurkiyaXitoySHOP"
    )


@bot.message_handler(
    func=lambda message: message.text == "📸 instagram:"
)
def instagram(message):
    bot.send_message(
        message.chat.id,
        "Instagram:\n"
        "https://www.instagram.com/dilshooda_/"
    )


@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)

    print("TELEGRAM UPDATE KELDI:", update)

    bot.process_new_updates([update])

    return 'ok', 200
if __name__ == '__main__':
    bot.remove_webhook()

    bot.set_webhook(
        url='https://dila-shoping-bot-1.onrender.com/webhook'
    )

    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000))
    )