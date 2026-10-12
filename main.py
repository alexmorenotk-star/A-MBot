import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
# ID del grupo de respaldo donde se copiará todo
BACKUP_CHAT_ID = -1003064360438  # <-- PON AQUI EL ID DE TU GRUPO DE RESPALDO

async def copiar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Reenviar cualquier mensaje al grupo de respaldo
        if update.message:
            await context.bot.forward_message(
                chat_id=BACKUP_CHAT_ID,
                from_chat_id=update.effective_chat.id,
                message_id=update.message.message_id
            )
    except Exception as e:
        print(f"Error: {e}")

def main():
    if not BOT_TOKEN:
        print("ERROR: No hay BOT_TOKEN en Environment")
        return
    
    print("Iniciando bot...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, copiar_mensaje))
    app.run_polling()

if __name__ == "__main__":
    main()
