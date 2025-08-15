import logging
from telegram.ext import Application, CommandHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "7566260613:AAFzyMo_3uumeEEqsPQEOtUjfUhFx_azTbM"
PORT = 10000  # Render will assign dynamically, but we use 10000 as fallback

# Start command
async def start(update, context):
    await update.message.reply_text("⚡ Welcome Warrior! Shinra AI is online. Type /mission to receive today’s mission.")

# Mission command
async def mission(update, context):
    await update.message.reply_text("🎯 Today’s Mission: 100 Pushups + 2 Hours Study + No Phone Distractions.\n\nStay disciplined!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("mission", mission))

    # 🚀 Use webhook instead of polling
    import os
    from flask import Flask, request

    app_flask = Flask(__name__)

    @app_flask.route(f"/{TOKEN}", methods=["POST"])
    def webhook():
        update = request.get_json(force=True)
        app.update_queue.put_nowait(update)
        return "OK"

    # Set webhook URL (your Render service URL)
    WEBHOOK_URL = f"https://Ai-san-shinra-bot-2/{TOKEN}"

    import telegram
    bot = telegram.Bot(TOKEN)
    bot.set_webhook(WEBHOOK_URL)

    app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", PORT)))

if __name__ == "__main__":
    main()
