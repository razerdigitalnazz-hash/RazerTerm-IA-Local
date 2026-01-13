from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from src.config import Config
from src.bot import iniciar, manejar_mensaje, callback_botones
import logging

# Configuración de logs para auditoría técnica
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

if __name__ == '__main__':
    # Validación de seguridad del Arquitecto
    if not Config.TOKEN_TELEGRAM:
        print("❌ ERROR CRÍTICO: No se encontró TELEGRAM_TOKEN en el .env")
        exit()

    # Construcción de la aplicación (v20+)
    app = ApplicationBuilder().token(Config.TOKEN_TELEGRAM).build()

    # Registro de rutas (Handlers)
    app.add_handler(CommandHandler("start", iniciar))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))
    app.add_handler(CallbackQueryHandler(callback_botones)) # Para los botones

    print(f"🚀 RazerTerm_IA iniciado correctamente")
    print(f"🖥️ Hardware: RX 570 (Vulkan) | Python 3.10.11")
    app.run_polling()
