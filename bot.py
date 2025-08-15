import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command
async def start(update, context):
    await update.message.reply_text(
        "⚡ Welcome Warrior! AI-San Shinra AI is online. Type /mission to receive today’s mission."
    )

# Mission command
async def mission(update, context):
    await update.message.reply_text(
        "🎯 Today’s Mission: 100 Pushups + 2 Hours Study + No Phone Distractions.\n\nStay disciplined!"
    )

# Echo fallback
async def echo(update, context):
    await update.message.reply_text("🔥 AI-San is listening… type /mission to begin!")

def main():
    # Replace with your real token
    application = Application.builder().token("7566260613:AAFzyMo_3uumeEEqsPQEOtUjfUhFx_azTbM").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("mission", mission))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == "__main__":
    main()
