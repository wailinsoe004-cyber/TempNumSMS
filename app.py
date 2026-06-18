import os
import time
import telebot

BOT_TOKEN = os.getenv(“BOT_TOKEN”)

if not BOT_TOKEN:
raise ValueError(“BOT_TOKEN not found”)

bot = telebot.TeleBot(BOT_TOKEN)

try:
bot.remove_webhook()
except:
pass

@bot.message_handler(commands=[“start”])
def start(message):
bot.reply_to(message, “✅ Railway Bot Online”)

while True:
try:
bot.infinity_polling(
timeout=120,
long_polling_timeout=120,
skip_pending=True
)
except Exception as e:
print(“Polling error:”, e)
time.sleep(10)
