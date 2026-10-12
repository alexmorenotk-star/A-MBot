import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# PEGA AQUI EL ID DE TU CANAL BÓVEDA (el que va a guardar todo)
BACKUP_CHAT_ID = -1003064360438  # <-- CAMBIA ESTO POR TU ID REAL

async def copiar_a_boveda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # No copiar lo que ya está en la bóveda para evitar bucle
        if update.effective_chat.id == BACKUP_CHAT_ID:
            return

        if update.message:
            await context.bot.forward_message(
                chat_id=BACKUP_CHAT_ID,
                from_chat_id=update.effective_chat.id,
                message_id=update.message.message_id
            )
            print(f"Copiado de {update.effective_chat.id} a Bóveda")
    except Exception as e:
        print(f"Error: {e}")

def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, copiar_a_boveda))
    print("Bóveda activa copiando todo...")
    app.run_polling()

if __name__ == "__main__":
    main()
