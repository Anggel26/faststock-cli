# FastStock CLI - Gestor de Inventario 🚀

**FastStock CLI** es una aplicación de consola desarrollada en Python diseñada para facilitar a los pequeños comercios la gestión de sus productos, el control de stock y la simulación de ventas de manera ágil.

Este proyecto surge para aplicar conocimientos técnicos en un entorno funcional, construyendo una herramienta robusta que demuestra capacidad en la resolución de problemas lógicos y gestión de datos.

---

## 📈 Evolución y Mejora Continua
Este repositorio es un "proyecto vivo". Actualmente, el desarrollo se encuentra en la **Fase 2**, enfocada en la robustez y profesionalización del código.

* ✅ **Fase 1:** Implementación de la lógica central y estructuras de datos dinámicas.
* 🚀 **Fase 2 (Actual):** **Modularización y Validación.** Refactorización mediante funciones independientes, control de flujo profesional con `if __name__ == "__main__":` y gestión de errores con `try-except`.
* ⏳ **Fase 3 (Próximamente):** Integración de persistencia de datos (guardado en archivos) y principios de Programación Orientada a Objetos (POO).

---

## ✨ Características de la Fase 2
- 📦 **Registro Validado:** Entrada de productos con protección contra datos nulos o tipos incorrectos (validación de números).
- 📋 **Inventario en Tiempo Real:** Visualización clara del estado actual de todos los productos.
- 🔄 **Actualización de Stock:** Sistema de búsqueda de productos por nombre para modificar existencias.
- 💰 **Simulador de Ventas:** Proceso automatizado que descuenta stock y calcula el total de la transacción.
- ⚠️ **Reporte de Stock Bajo:** Alertas automáticas para productos con existencias críticas (menos de 5 unidades).

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Lógica:** Funciones modulares, manejo de excepciones, listas de diccionarios y tipos de datos primitivos.

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