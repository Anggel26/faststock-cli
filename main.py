"""FastStock CLI - Gestor de inventario y ventas.

Refactorizaciones principales:
- Encapsulado de entradas numéricas con validación.
- Funciones para registrar, listar, actualizar y vender productos.
- Búsqueda reutilizable de productos por nombre.
"""

print("Bienvenido a FastStock CLI (Gestor de Inventario y Ventas)")

inventario = []


def input_int(prompt, min_value=None):
    while True:
        try:
            v = int(input(prompt))
            if min_value is not None and v < min_value:
                print(f"Ingrese un número mayor o igual a {min_value}.")
                continue
            return v
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")


def input_float(prompt, min_value=None):
    while True:
        try:
            v = float(input(prompt))
            if min_value is not None and v < min_value:
                print(f"Ingrese un número mayor o igual a {min_value}.")
                continue
            return v
        except ValueError:
            print("Entrada no válida. Ingrese un número (por ejemplo 12.50).")


def mostrar_menu():
    print("\nMenú principal:")
    print("1. Registrar nuevos productos")
    print("2. Listar inventario")
    print("3. Actualizar stock")
    print("4. Simular venta")
    print("5. Reporte de stock bajo")
    print("6. Salir")


def registrar_producto(inventario):
    print("\nRegistro de producto.")
    while True:
        nombre = input("Nombre del producto: ").strip()
        precio = input_float("Precio: ", min_value=0)
        cantidad = input_int("Cantidad inicial: ", min_value=0)

        producto = {"nombre": nombre, "precio": precio, "stock": cantidad}
        inventario.append(producto)
        print(f"{nombre} añadido al inventario.")

        if input("¿Desea registrar otro producto? (s/n): ").lower() != "s":
            break


def listar_inventario(inventario):
    print("\nInventario actual:")
    if not inventario:
        print("El inventario está vacío.")
        return
    for p in inventario:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']}")


def seleccionar_producto(inventario, prompt):
    """Pide por nombre hasta encontrar un producto o el usuario escriba 'salir'.
    Devuelve el diccionario del producto o None si el usuario cancela."""
    while True:
        buscar = input(prompt).strip()
        if buscar.lower() == "salir":
            return None
        for p in inventario:
            if p["nombre"].lower() == buscar.lower():
                return p
        print("Producto no encontrado, inténtelo de nuevo o escriba 'salir'.")


def actualizar_stock(inventario):
    p = seleccionar_producto(inventario, "Nombre del producto a actualizar (escribe 'salir' para volver): ")
    if not p:
        return
    sumar = input_int(f"Cantidad a sumar al stock de {p['nombre']}: ", min_value=0)
    p["stock"] += sumar
    print("Stock actualizado.")


def simular_venta(inventario):
    p = seleccionar_producto(inventario, "Producto que desea vender (escribe 'salir' para volver): ")
    if not p:
        return
    while True:
        cantidad = input_int(f"Cantidad a vender de {p['nombre']}: ", min_value=0)
        if cantidad <= p["stock"]:
            p["stock"] -= cantidad
            total = cantidad * p["precio"]
            print(f"Venta realizada. Total: ${total}")
            return
        print("No hay suficiente stock. Intente con una cantidad menor.")


def reporte_stock_bajo(inventario, umbral=5):
    bajos = [p for p in inventario if p["stock"] < umbral]
    if not bajos:
        print("No hay productos con stock bajo.")
        return
    print("Productos con stock bajo:")
    for p in bajos:
        print(f"Producto: {p['nombre']} | reporta {p['stock']} unidades.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Por favor, digite la opción que desea: ").strip()
        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            listar_inventario(inventario)
        elif opcion == "3":
            actualizar_stock(inventario)
        elif opcion == "4":
            simular_venta(inventario)
        elif opcion == "5":
            reporte_stock_bajo(inventario)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción incorrecta, inténtelo de nuevo.")


if __name__ == "__main__":
    main()