# FastStock CLI - Gestor de Inventario 🚀

**FastStock CLI** es una aplicación de consola desarrollada en Python diseñada para facilitar a los pequeños comercios la gestión de sus productos, el control de stock y la simulación de ventas de manera ágil.

Este proyecto surge para mejorar mis habilidades como desarrollador, transformando scripts básicos en software estructurado y profesional.

---

## 📈 Evolución y Mejora Continua
Este repositorio es un "proyecto vivo". Actualmente, acabamos de implementar la **Fase 4**, migrando a una **Arquitectura en Capas**.

* ✅ **Fase 1:** Implementación lógica básica y estructuras de datos.
* ✅ **Fase 2:** Modularización, validación de entradas y manejo de errores.
* ✅ **Fase 3:** **Programación Orientada a Objetos (POO).** Clases `Producto`, encapsulamiento y uso de `lambda`.
* ✅ **Fase 4:** **Arquitectura en Capas y Persistencia.** Refactorización del código monolítico.
* ✅ **Fase 5:** **Reportes Avanzados y Análisis de Datos.**
    * **Historial de Ventas:** Registro detallado de cada movimiento y venta.
    * **Reportes Temporales:** Generación de reportes de ventas por mes, semana o día.
    * **Análisis de Ganancias:** Cálculo de márgenes reales (Precio Venta - Costo Compra).
    * **Exportación de Datos:** Capacidad de exportar reportes a CSV.

---

## ✨ Características Nuevas (Versión 4.0 - Data Analysis & UX)
- 📊 **Módulo de Reportes:** Visualiza tus ingresos, costos y ganancias netas por día o mes.
- 💰 **Control de Costos:** Ahora puedes registrar el "Costo de Compra" de cada producto para saber cuánto estás ganando realmente.
- 🛡️ **Validaciones Inteligentes:** El sistema previene nombres duplicados, alerta sobre ventas a pérdida y protege la integridad de los datos.
- 📂 **Organización de Datos:** Todos los archivos de persistencia (`inventario.txt`, `ventas.txt`) ahora viven ordenadamente en la carpeta `data/`.
- 🔄 **Gestión Flexible:** Ajusta tu stock hacia arriba o abajo y actualiza costos en cualquier momento.

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.10+
- **Arquitectura:** Layered Architecture (Models, Repositories, Services, UI)
- **Persistencia:** File System (Structured TXT/CSV in `data/` directory)

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

---

## 📢 Feedback

¡Estoy aprendiendo y mejorando constantemente! Si tienes sugerencias, encuentras errores o quieres recomendar mejores prácticas, por favor abre un **Issue** o contáctame. ¡Cualquier feedback es bienvenido!
