from telegram.ext import ApplicationBuilder, CommandHandler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import os

from odds_fetcher import check_odds
from news_fetcher import check_news

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def start(update, context):
    await update.message.reply_text("Vedonlyöntibotti on käynnissä!")

async def odds_job(app):
    message = check_odds()
    if message:
        await app.bot.send_message(chat_id=CHAT_ID, text=message)

async def news_job(app):
    message = check_news()
    if message:
        await app.bot.send_message(chat_id=CHAT_ID, text=message)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    scheduler = AsyncIOScheduler()
    scheduler.add_job(lambda: odds_job(app), "interval", seconds=600)
    scheduler.add_job(lambda: news_job(app), "interval", seconds=1800)
    scheduler.start()

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
