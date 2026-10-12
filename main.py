import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# CONFIGURACION
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GRUPO_RESPALDO = -1004291723463

MAPEO = {
    -1004429727366: (GRUPO_RESPALDO, 5),
    -1004416790061: (GRUPO_RESPALDO, 3),
    -1003986268078: (GRUPO_RESPALDO, 4),
}

logging.basicConfig(level=logging.INFO)

async def reenviar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post or update.message
    if not msg:
        return
    origen = msg.chat.id
    if origen in MAPEO:
        destino, thread_id = MAPEO[origen]
        try:
            await context.bot.copy_message(
                chat_id=destino,
                from_chat_id=origen,
                message_id=msg.message_id,
                message_thread_id=thread_id
            )
            print(f"Enviado de {origen} a {destino}")
        except Exception as e:
            print(f"Error: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, reenviar))
    print("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
