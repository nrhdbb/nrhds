import telebot
import os

# Gunakan environment variable untuk API Token
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Command untuk mulai bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Saya adalah Parental Control Bot.\nGunakan /lokasi untuk mendapatkan lokasi anak.")

# Command untuk mendapatkan lokasi anak
@bot.message_handler(commands=['lokasi'])
def send_location(message):
    lat, lon = -6.2088, 106.8456  # Contoh lokasi Jakarta
    maps_link = f"https://www.google.com/maps?q={lat},{lon}"
    bot.send_message(message.chat.id, f"📍 Lokasi Anak:\n{maps_link}")

# Looping bot agar tetap berjalan
bot.polling()
