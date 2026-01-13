import httpx
from .config import Config

async def consultar_ia(texto_usuario, entorno="Python", modo="Normal"):
    conf = Config.MODELOS.get(Config.MODELO_ACTUAL)
    
    # Selección de instrucción según el botón o comando
    if modo == "Normal":
        instruccion = Config.PROMPTS.get(entorno, "Solo entrega código.")
    else:
        instruccion = Config.PROMPTS.get(modo, "Solo entrega código.")

    prompt_final = conf["template"].format(instruccion, texto_usuario)
    
    payload = {
        "prompt": prompt_final,
        "max_context_length": 2048,
        "max_length": 450, # límite seguro para RX 570
        "temperature": 0.1 if modo != "Otra" else 0.7, # Más variedad si pide "Otra versión"
        "top_p": 0.9,
        "stop": conf["stop"]
    }

    async with httpx.AsyncClient(timeout=None) as client:
        try:
            response = await client.post(Config.URL_KOBOLD, json=payload)
            if response.status_code == 200:
                return response.json()['results'][0]['text'].strip()
            return f"❌ Error de API: {response.status_code}"
        except Exception as e:
            return f"⚠️ Error de conexión: {e}"
