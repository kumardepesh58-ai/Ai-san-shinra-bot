import logging
import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "7566260613:AAFzyMo_3uumeEEqsPQEOtUjfUhFx_azTbM"
PORT = int(os.environ.get("PORT", 10000))
WEBHOOK_URL = f"https://ai-san-shinra-bot-2.onrender.com/{TOKEN}"

app_flask = Flask(__name__)
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Welcome Warrior! Shinra AI is online. Type /mission to receive today’s mission."
    )

async def mission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 Today’s Mission: 100 Pushups + 2 Hours Study + No Phone Distractions.\n\nStay disciplined!"
    )

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("mission", mission))

# Use the existing event loop
@app_flask.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.get_event_loop().create_task(application.process_update(update))
    return "OK"

if __name__ == "__main__":
    bot = Bot(TOKEN)
    bot.set_webhook(WEBHOOK_URL)
    app_flask.run(host="0.0.0.0", port=PORT)
