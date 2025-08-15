import logging
import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "7566260613:AAFzyMo_3uumeEEqsPQEOtUjfUhFx_azTbM"
PORT = int(os.environ.get("PORT", 10000))
WEBHOOK_URL = f"https://ai-san-shinra-bot-2.onrender.com/{TOKEN}"

# Flask app
app_flask = Flask(__name__)

# Telegram app
application = Application.builder().token(TOKEN).build()

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Welcome Warrior! Shinra AI is online. Type /mission to receive today’s mission."
    )

# Mission command
async def mission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 Today’s Mission: 100 Pushups + 2 Hours Study + No Phone Distractions.\n\nStay disciplined!"
    )

# Add handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("mission", mission))

# Correct webhook route
@app_flask.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.create_task(application.process_update(update))
    return "OK"

if __name__ == "__main__":
    # Set webhook
    bot = Bot(TOKEN)
    bot.set_webhook(WEBHOOK_URL)

    # Run Flask server
    app_flask.run(host="0.0.0.0", port=PORT)
