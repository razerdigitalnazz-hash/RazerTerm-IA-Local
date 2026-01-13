from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from .conector import consultar_ia
from .config import Config
import time

# Teclado físico de acceso rápido
TECLADO_MENU = ReplyKeyboardMarkup(
    [['🪟 CMD', '🐧 Bash', '🐍 Python'], ['ℹ️ Ayuda']],
    resize_keyboard=True
)

async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bienvenida inicial y reseteo de tiempo"""
    context.user_data['saludado'] = True
    context.user_data['ultimo_contacto'] = time.time()
    await update.message.reply_text(Config.BIENVENIDA, parse_mode='Markdown', reply_markup=TECLADO_MENU)

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manejador principal con lógica de cortesía y tiempo (2026)"""
    user_text = update.message.text
    if not user_text: return
    text_lower = user_text.lower().strip()
    
    # 1. PRIORIDAD: LÓGICA DE GRATITUD (No consume tokens de IA)
    palabras_gracias = ["gracias", "muchas gracias", "listo", "terminamos", "perfecto", "buenisimo"]
    if any(p in text_lower for p in palabras_gracias):
        keyboard = [[InlineKeyboardButton("⭐ ¡Todo funcional!", callback_data='task_Conforme')]]
        await update.message.reply_text(Config.MSJ_GRACIAS, reply_markup=InlineKeyboardMarkup(keyboard))
        return

    # 2. LÓGICA DE INACTIVIDAD (5 MINUTOS)
    ahora = time.time()
    ultimo_visto = context.user_data.get('ultimo_contacto', ahora)
    if ahora - ultimo_visto > 300: # 300 segundos = 5 min
        await update.message.reply_text(Config.MSJ_RECONEXION, parse_mode='Markdown', reply_markup=TECLADO_MENU)
        context.user_data['ultimo_contacto'] = ahora
        return
    
    context.user_data['ultimo_contacto'] = ahora 

    # --- MEJORA V1: DETECCIÓN DE BOTÓN AYUDA ---
    if "ℹ️ ayuda" in text_lower:
        await update.message.reply_text(
            Config.AYUDA_SISTEMA, 
            parse_mode='HTML',
            reply_markup=TECLADO_MENU
        )
        return

    # 3. LÓGICA DE SALUDOS
    saludos = ["hola", "buenas", "hey", "hola!", "buen día"]
    if text_lower in saludos:
        if context.user_data.get('saludado'):
            await update.message.reply_text("👋 Aquí estoy de nuevo. ¿Quieres un comando para CMD, Bash o un bloque de Python?")
        else:
            await iniciar(update, context)
        return

    # 4. LÓGICA DE PREFIJOS DIRECTOS
    entorno = None
    peticion_ia = user_text
    if text_lower.startswith("python:"): 
        entorno, peticion_ia = "Python", user_text[7:]
    elif text_lower.startswith("bash:"): 
        entorno, peticion_ia = "Bash", user_text[5:]
    elif text_lower.startswith("cmd:"): 
        entorno, peticion_ia = "CMD", user_text[4:]

    if entorno:
        await procesar_y_responder(update, context, peticion_ia.strip(), entorno)
    else:
        # Si no hay prefijo ni es cortesía, preguntamos el entorno
        context.user_data['peticion_actual'] = user_text
        keyboard = [[
            InlineKeyboardButton("🐍 Python", callback_data='env_Python'),
            InlineKeyboardButton("🐧 Bash", callback_data='env_Bash'),
            InlineKeyboardButton("🪟 CMD", callback_data='env_CMD')
        ]]
        await update.message.reply_text("🛠️ Selecciona el entorno:", reply_markup=InlineKeyboardMarkup(keyboard))

async def callback_botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestión de botones inline (Mantiene lógica de no-borrado)"""
    query = update.callback_query
    data = query.data
    await query.answer()

    # Botón de conformidad de gratitud
    if data == 'task_Conforme':
        await query.edit_message_text("✨ ¡Excelente noticia! Aquí estaré para tu próxima tarea. 🐧")
        return

    # Selección de entorno inicial
    if data.startswith("env_"):
        entorno = data.split("_")[1]
        peticion = context.user_data.get('peticion_actual')
        await query.edit_message_text(f"⚡ <b>Generando para {entorno}...</b>", parse_mode='HTML')
        await procesar_y_responder(query, context, peticion, entorno)

    # Tareas (Otra versión, Corto, Explicar)
    elif data.startswith("task_"):
        partes = data.split("_")
        modo, entorno = partes[1], partes[2]
        ultimo_codigo = context.user_data.get('ultimo_codigo', '')
        
        # MANTENEMOS: Explicar en mensaje nuevo para no borrar el código
        if modo == "Explicar":
            aviso = await query.message.reply_text(f"🧠 <b>Analizando código...</b>", parse_mode='HTML')
            respuesta = await consultar_ia(ultimo_codigo, entorno, modo)
            await query.message.reply_text(f"🧠 <b>Explicación Técnica:</b>\n\n{respuesta}", parse_mode='HTML')
            await aviso.delete()
        else:
            # Para "Otra versión" o "Corto" editamos el bloque existente
            await query.edit_message_text(f"⏳ <b>Actualizando código ({modo})...</b>", parse_mode='HTML')
            respuesta = await consultar_ia(ultimo_codigo, entorno, modo)
            await enviar_resultado_final(query, context, respuesta, entorno)

async def procesar_y_responder(update_or_query, context, peticion, entorno):
    respuesta = await consultar_ia(peticion, entorno)
    await enviar_resultado_final(update_or_query, context, respuesta, entorno)

async def enviar_resultado_final(target, context, respuesta, entorno):
    """Formato HTML seguro para RX 570 (Mantiene lógica funcional anterior)"""
    context.user_data['ultimo_codigo'] = respuesta
    keyboard = [
        [InlineKeyboardButton("🔁 Otra versión", callback_data=f"task_Otra_{entorno}"),
         InlineKeyboardButton("✂️ Más corto", callback_data=f"task_Corto_{entorno}")],
        [InlineKeyboardButton("🧠 Explicar", callback_data=f"task_Explicar_{entorno}")]
    ]
    
    # Escapado de caracteres para evitar error 400 Bad Request
    safe_res = respuesta.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    mensaje = f"⌨️ <b>RESULTADO ({entorno})</b>\n\n<pre>{safe_res}</pre>\n\n💡 <i>Toca para copiar.</i>"
    
    if hasattr(target, 'edit_message_text'):
        await target.edit_message_text(mensaje, parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await target.message.reply_text(mensaje, parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
