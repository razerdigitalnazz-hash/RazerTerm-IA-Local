# ?? RazerTerm_IA (v1.0): Agente de Asistencia de C車digo Accesible

> **Estado:** Alpha v1.0 | **Plataforma:** Telegram Bot | **Backend:** Local (Python + Koboldcpp)

**RazerTerm_IA** es un asistente inteligente dise?ado para democratizar el acceso a la programaci車n. Funciona como un "Compa?ero de C車digo" accesible directamente desde Telegram, permitiendo a desarrolladores generar, corregir y consultar snippets de c車digo al instante, sin depender de interfaces web pesadas.

## ?? Objetivo del Proyecto
Crear una herramienta de **accesibilidad universal** para programadores. Al ejecutarse en Telegram, permite obtener ayuda de codificaci車n incluso con conexiones lentas o desde dispositivos m車viles b芍sicos, procesando toda la inteligencia en un servidor local optimizado.

## ??? Infraestructura & Optimizaci車n (Legacy Hardware)
Este proyecto demuestra que la IA es viable en hardware reutilizado mediante ingenier赤a de software eficiente.

* **CPU:** Intel Core i3-2120 (2.a Gen - Sandy Bridge).
* **GPU:** AMD Radeon RX 570 4GB (Vulkan/ROCm).
* **RAM:** 16GB DDR3.
* **Sistema Operativo:** H赤brido (Desarrollado en Windows / Desplegado en Xubuntu).
* **Optimizaciones:** Arquitectura as赤ncrona (`asyncio` + `httpx`) para evitar cuellos de botella en el i3 durante la inferencia neuronal.

## ?? Roadmap: ?Qu谷 viene en la v1.1?
Este agente est芍 en evoluci車n constante. Las pr車ximas actualizaciones incluir芍n:
* ? **Asistente Git:** Generaci車n autom芍tica de comandos para control de versiones (`git push`, `commit`, `branch`).
* ? **Refactorizaci車n:** M車dulo para limpiar y optimizar c車digo sucio.
* ? **Modo Docker:** Despliegue autom芍tico del bot en contenedores.

## ??? Stack Tecnol車gico
* **Python 3.10**
* **Telegram Bot API (v20+)**
* **Koboldcpp (GGUF Models)**