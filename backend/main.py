from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8158342090:AAEeMV9W8c267_Aa0n7ikGFIbCapZg-dzbk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏁 Добро пожаловать в Night Rush!\nНажми, чтобы запустить игру:\n"
        "👉 https://<your-app-name>.onrender.com"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()