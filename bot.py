import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Hae bot token ympäristömuuttujasta
BOT_TOKEN = os.getenv("BOT_TOKEN")

# /start komennon käsittelijä
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hei! Vedonlyöntibotti on nyt käynnissä.")

async def main():
    # Luo botti-application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Lisää handler /start-komennolle
    app.add_handler(CommandHandler("start", start))

    # Käynnistä botti ja aloita kuuntelu
    await app.run_polling()


   
