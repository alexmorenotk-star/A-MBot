import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ChannelPostHandler, filters, ContextTypes

async def mostrar_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print(f"ID detectado: {chat_id}")
    # Intenta responder donde se pueda
    try:
        if update.message:
            await update.message.reply_text(f"ID: {chat_id}")
        elif update.channel_post:
            await update.channel_post.reply_text(f"ID: {chat_id}")
    except:
        pass

def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, mostrar_id))
    app.add_handler(ChannelPostHandler(mostrar_id))
    app.run_polling()

if __name__ == "__main__":
    main()
