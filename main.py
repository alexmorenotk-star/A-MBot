import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

async def mostrar_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print(f"ID detectado: {chat_id}")
    try:
        if update.message:
            await update.message.reply_text(f"ID: {chat_id}")
        if update.channel_post:
            await update.channel_post.reply_text(f"ID: {chat_id}")
        # Para grupos con temas
        if update.effective_message:
            await update.effective_message.reply_text(f"ID: {chat_id}")
    except Exception as e:
        print(f"Error enviando: {e}")

def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()
    # Detecta mensajes normales y de canal/temas
    app.add_handler(MessageHandler(filters.ALL, mostrar_id))
    app.run_polling()

if __name__ == "__main__":
    main()
