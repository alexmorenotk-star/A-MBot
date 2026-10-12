import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

VAULT_ID = -1004291723463

async def respaldo_automatico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post or update.message
    if not msg:
        return

    origen_id = update.effective_chat.id
    if origen_id == VAULT_ID:
        return

    try:
        await context.bot.copy_message(
            chat_id=VAULT_ID,
            message_thread_id=1,
            from_chat_id=origen_id,
            message_id=msg.message_id
        )
        print(f"Respaldo OK de {origen_id}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, respaldo_automatico))
    app.run_polling()

if __name__ == "__main__":
    main()
