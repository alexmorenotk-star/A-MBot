import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

VAULT_ID = -1004291723463

# --- Truco para que Render no falle ---
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
    print("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
