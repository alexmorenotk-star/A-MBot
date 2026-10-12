import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# BÓVEDA - Aquí cae todo
VAULT_ID = -1004291723463

# --- Truco para que funcione en el plan GRATIS de Render ---
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot activo")

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()
# --- Fin del truco ---

async def respaldo_universal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Funciona tanto para canales como para grupos
    msg = update.channel_post or update.message
    if not msg:
        return
    
    origen_id = update.effective_chat.id
    
    # Evitar bucle infinito (que no se respalde a sí mismo)
    if origen_id == VAULT_ID:
        return

    try:
        # Copia tal cual a la bóveda
        await context.bot.copy_message(
            chat_id=VAULT_ID,
            from_chat_id=origen_id,
            message_id=msg.message_id
        )
        print(f"Respaldo OK desde {origen_id}")
    except Exception as e:
        print(f"Error respaldando: {e}")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Falta BOT_TOKEN")
        return
        
    app = Application.builder().token(token).build()
    # Escucha TODO lo que se suba en cualquier canal donde esté
    app.add_handler(MessageHandler(filters.ALL, respaldo_universal))
    print("Bot iniciado... esperando archivos")
    app.run_polling()

if __name__ == "__main__":
    main()
