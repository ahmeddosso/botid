import telebot
import os

TOKEN = os.getenv("7916400505:AAFbwOGC-HIucdQSh6Lc7YSzfrWzg0pAMSk")  # On récupère le token via les variables d’environnement
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Yo bg, je suis en ligne sur Render ! 🔥")

bot.polling()
