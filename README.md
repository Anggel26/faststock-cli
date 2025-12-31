# FastStock CLI - Gestor de Inventario 🚀

**FastStock CLI** es una aplicación de consola desarrollada en Python diseñada para facilitar a los pequeños comercios la gestión de sus productos, el control de stock y la simulación de ventas de manera ágil.

Este proyecto surge para mejorar mis habilidades como desarrollador, transformando scripts básicos en software estructurado y profesional.

---

## 📈 Evolución y Mejora Continua
Este repositorio es un "proyecto vivo". Actualmente, acabamos de implementar la **Fase 4**, migrando a una **Arquitectura en Capas**.

* ✅ **Fase 1:** Implementación lógica básica y estructuras de datos.
* ✅ **Fase 2:** Modularización, validación de entradas y manejo de errores.
* ✅ **Fase 3:** **Programación Orientada a Objetos (POO).** Clases `Producto`, encapsulamiento y uso de `lambda`.
* 🚀 **Fase 4 (Actual):** **Arquitectura en Capas y Persistencia.** Refactorización del código monolítico a una estructura escalable:
    * **Modelos:** Definición de datos (`app/models`).
    * **Repositorios:** Capa de acceso a datos y persistencia en archivo (`app/repositories`).
    * **Servicios:** Lógica de negocio (`app/services`).
    * **UI:** Interfaz de consola separada de la lógica (`app/ui`).
* ⏳ **Fase 5 (Próximamente):** **Reportes Avanzados y Análisis de Datos.**
    * **Historial de Ventas:** Registro detallado de cada movimiento y venta.
    * **Reportes Temporales:** Generación de reportes de ventas por mes, semana o día.
    * **Análisis de Ganancias:** Cálculo de márgenes y beneficios en periodos determinados.
    * **Exportación de Datos:** Capacidad de exportar reportes a TXT.

---

## ✨ Características Nuevas (Versión 3.0 - Layered Architecture)
- 🏗️ **Diseño Modular:** Separación clara de responsabilidades lo que facilita el mantenimiento y escalabilidad.
- � **Persistencia Automática:** Los datos se guardan y cargan automáticamente al iniciar la aplicación.
- 🛡️ **Validación Robusta:** Sistema centralizado de validación de entradas.

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Arquitectura:** MVC / Layered (Models, Repositories, Services, UI)
- **Persistencia:** File System (TXT/CSV based structures)

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