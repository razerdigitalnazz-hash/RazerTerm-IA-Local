import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TOKEN_TELEGRAM = os.getenv("TELEGRAM_TOKEN")
    URL_KOBOLD = "http://localhost:5001/api/v1/generate"
    MODELO_ACTUAL = "llama3" 

    MODELOS = {
        "phi3": {
            "template": "<|system|>\n{}<|end|>\n<|user|>\n{}<|end|>\n<|assistant|>\n",
            "stop": ["<|end|>", "<|user|>", "<|assistant|>"]
        },
        "llama3": {
            "template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
            "stop": ["<|eot_id|>", "<|start_header_id|>"]
        }
    }

    # Prompts ultra-específicos para ahorrar VRAM
    PROMPTS = {
        "Python": "Rol: Programador Python 3.10. Tarea: Solo código compacto, máximo 15 líneas, sin comentarios. Si es complejo, usa funciones básicas.",
        "Bash": "Rol: Experto Linux. Tarea: Solo comandos Bash, máximo 3-5 líneas. Sin explicaciones.",
        "CMD": "Rol: Experto Windows CMD. Tarea: Solo comandos batch, máximo 5 líneas.",
        "Explicar": "Rol: Tutor técnico. Tarea: Explica el código anterior en 3 puntos breves y técnicos.",
        "Corto": "Tarea: Reescribe el código anterior en el menor número de líneas posible (Code Golf)."
    }

    BIENVENIDA = (
        "👋 **Hola, soy tu asistente de comandos y código.**\n\n"
        "Puedo ayudarte con:\n"
        "🪟 **CMD** (Windows)\n"
        "🐧 **Bash** (Linux)\n"
        "🐍 **Python** (Funciones atómicas)\n\n"
        "Escribe directamente tu duda o usa: `python: mi tarea`"
    )

    # --- NUEVOS MENSAJES DE CORTESÍA ---
    MSJ_GRACIAS = (
        "¡De nada! Es un placer ayudarte con el código. 😊\n\n"
        "¿El resultado fue funcional para tu sistema?"
    )
    
    MSJ_RECONEXION = (
        "🔄 **¡Hola de nuevo! He refrescado mis procesos.**\n\n"
        "¿En qué sistema trabajaremos ahora?"
    )

    # --- MEJORA V1: MANUAL DE OPERACIONES ---
    AYUDA_SISTEMA = (
        "🚀 <b>MODO DE USO: RAZERTERM_IA</b>\n\n"
        "1. <b>Petición:</b> Escribe tu duda técnica directamente.\n"
        "2. <b>Entorno:</b> Elige el sistema (Python, Bash o CMD).\n"
        "3. <b>Código:</b> Copia el resultado atómico generado.\n\n"
        "✨ <b>Extras:</b> Usa los botones bajo el código para explicarlo, "
        "acortarlo o ver una versión alternativa.\n\n"
        "<i>Hardware: RX 570 (Vulkan) | Estado: Operativo</i>"
    )
