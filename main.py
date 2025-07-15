import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from backend.config import BOT_TOKEN
from backend.handlers import start, help_command

logging.basicConfig(level=logging.INFO)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
