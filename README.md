# FastStock CLI - Gestor de Inventario 🚀

**FastStock CLI** es una aplicación de consola desarrollada en Python diseñada para facilitar a los pequeños comercios la gestión de sus productos, el control de stock y la simulación de ventas de manera ágil.

Este proyecto surge para mejorar mis habilidades como desarrollador, transformando scripts básicos en software estructurado y profesional.

---

## 📈 Evolución y Mejora Continua
Este repositorio es un "proyecto vivo". Actualmente, acabamos de implementar la **Fase 3**, introduciendo paradigmas de diseño profesional.

* ✅ **Fase 1:** Implementación lógica básica y estructuras de datos.
* ✅ **Fase 2:** Modularización, validación de entradas y manejo de errores.
* 🚀 **Fase 3 (Actual):** **Programación Orientada a Objetos (POO).** Migración de diccionarios a clases robustas (**Producto**), uso de métodos mágicos (**__str__**) encapsulamiento, y optimización con funciones lambda.

---

## ✨ Características Nuevas (Versión 2.0)
- 🧠 **Arquitectura POO:** El sistema ahora maneja objetos **Producto** reales en lugar de diccionarios dispersos, lo que reduce errores y mejora la legibilidad.
- 🔍 **Búsquedas Inteligentes:** Lógica de búsqueda encapsulada y reutilizable para ventas y actualizaciones.
- 📊 **Reportes Avanzados:** Uso de **Programación Funcional** (`filter` + `lambda`) para generar reportes de stock bajo eficientes y limpios.
- 🛡️ **Validación Robusta:** Helpers dedicados (**input_int**, **input_float**) que garantizan que los datos numéricos sean siempre correctos.

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Lógica:** POO (Clases, Métodos, Instancias), Lambdas, Manejo de Excepciones y Listas de Objetos.

---

## 🚀 Guía de Instalación y Ejecución

Para ejecutar este proyecto en tu computadora, sigue estos pasos:

### 1. Requisitos Previos
Asegúrate de tener instalado **Python 3.10** o superior. 
- Puedes descargarlo en [python.org](https://www.python.org/).
- Verifica tu instalación abriendo una terminal y escribiendo: `python --version`

### 2. Obtención del Proyecto

Copia y pega estos comandos en tu terminal:

```bash
# 1. Clonar el repositorio desde GitHub
git clone https://github.com/Anggel26/faststock-cli.git

# 2. Entrar a la carpeta del proyecto
cd faststock-cli

# 3. Ejecutar la aplicación
# En Windows:
python main.py

# En macOS o Linux:
python3 main.py
```