# 🚀 RazerTerm_IA (v1.0): Agente de Asistencia de Código Accesible

> **Estado:** Alpha v1.0 | **Plataforma:** Telegram Bot | **Backend:** Local (Python + Koboldcpp)

**RazerTerm_IA** es un asistente inteligente diseñado para democratizar el acceso a la programación. Funciona como un "Compañero de Código" accesible directamente desde Telegram, permitiendo a desarrolladores generar, corregir y consultar snippets de código al instante, sin depender de interfaces web pesadas.

## 🎯 Objetivo del Proyecto
Crear una herramienta de **accesibilidad universal** para programadores. Al ejecutarse en Telegram, permite obtener ayuda de codificación incluso con conexiones lentas o desde dispositivos móviles básicos, procesando toda la inteligencia en un servidor local optimizado.

## 🖥️ Infraestructura & Optimización (Legacy Hardware)
Este proyecto demuestra que la IA es viable en hardware reutilizado mediante ingeniería de software eficiente.

* **CPU:** Intel Core i3-2120 (2.ª Gen - Sandy Bridge).
* **GPU:** AMD Radeon RX 570 4GB (Vulkan/ROCm).
* **RAM:** 16GB DDR3.
* **Sistema Operativo:** Híbrido (Desarrollado en Windows / Desplegado en Xubuntu).
* **Optimizaciones:** Arquitectura asíncrona (`asyncio` + `httpx`) para evitar cuellos de botella en el i3 durante la inferencia neuronal.

## 🔮 Roadmap: ¿Qué viene en la v1.1?
Este agente está en evolución constante. Las próximas actualizaciones incluirán:
* ✅ **Asistente Git:** Generación automática de comandos para control de versiones (`git push`, `commit`, `branch`).
* ✅ **Refactorización:** Módulo para limpiar y optimizar código sucio.
* ✅ **Modo Docker:** Despliegue automático del bot en contenedores.

## 🛠️ Stack Tecnológico
* **Python 3.10**
* **Telegram Bot API (v20+)**
* **Koboldcpp (GGUF Models)**
