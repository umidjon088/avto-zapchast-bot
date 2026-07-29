from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "BU_YERGA_BOT_TOKENINGIZ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! CHAMAN Auto Parts botiga xush kelibsiz."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
