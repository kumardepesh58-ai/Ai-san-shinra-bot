import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Start command
def start(update, context):
    update.message.reply_text("⚡ Welcome Warrior! AI-San Shinra AI is online. Type /mission to receive today’s mission.")

# Mission command
def mission(update, context):
    update.message.reply_text("🎯 Today’s Mission: 100 Pushups + 2 Hours Study + No Phone Distractions.\n\nStay disciplined!")

# Echo fallback
def echo(update, context):
    update.message.reply_text("🔥 AI-San is listening… type /mission to begin!")

def main():
    # Replace with your real token
    updater = Updater("7566260613:AAFzyMo_3uumeEEqsPQEOtUjfUhFx_azTbM", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("mission", mission))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
