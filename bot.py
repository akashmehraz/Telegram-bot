from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot.")

app = ApplicationBuilder().token("8048656674:AAECRx8plUshMWbW1v9Fn4iX20vaytoXNWI").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
