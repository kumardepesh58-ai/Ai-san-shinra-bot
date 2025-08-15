import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7566260613:AAFzyMo_3uumeEEqsPQEOtUjfUhFx_azTbM"
PORT = int(os.environ.get("PORT", 10000))
WEBHOOK_URL = f"https://ai-san-shinra-bot-2.onrender.com/{TOKEN}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Welcome Warrior! Shinra AI is online. Type /mission to receive today’s mission."
    )

async def mission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 Today’s Mission: 100 Pushups + 2 Hours Study + No Phone Distractions.\n\nStay disciplined!"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("mission", mission))

if __name__ == "__main__":
    # Start the bot with webhook
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=WEBHOOK_URL
    )
