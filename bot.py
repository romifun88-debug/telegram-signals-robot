from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "PON_AQUI_TU_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot activo\n\n"
        "📊 Señales GRATIS\n"
        "💎 Señales PREMIUM\n\n"
        "Usá /help"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/senal - señal demo\n"
        "/premium - info premium"
    )

async def senal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 SEÑAL DEMO\nEUR/USD\nCALL\n1 min"
    )

async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💎 PREMIUM\nContactame por Telegram"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("senal", senal))
    app.add_handler(CommandHandler("premium", premium))
    app.run_polling()

if __name__ == "__main__":
    main()
