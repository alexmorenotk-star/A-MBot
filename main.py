import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def mostrar_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"----> CHAT ID ES: {update.effective_chat.id} | Nombre: {update.effective_chat.title}")
    await update.message.reply_text(f"El ID de este chat es: {update.effective_chat.id}")

def main():
    app = Application.builder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(MessageHandler(filters.ALL, mostrar_id))
    print("Bot de IDs iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
