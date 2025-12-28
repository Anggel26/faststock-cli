"""FastStock CLI - Gestor de inventario y ventas (Versión POO)."""

class Producto:
    # Definimos la estructura básica de nuestro producto
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Método para mostrar el producto de forma legible
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}"


def input_int(prompt, minimo=None):
    # Función auxiliar para asegurar que recibimos un entero válido
    while True:
        try:
            v = int(input(prompt))
            if minimo is not None and v < minimo:
                print(f"Ingrese un número mayor o igual a {minimo}.")
                continue
            return v
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")


def input_float(prompt, minimo=None):
    # Función auxiliar para asegurar que recibimos un precio válido
    while True:
        try:
            v = float(input(prompt))
            if minimo is not None and v < minimo:
                print(f"Ingrese un número mayor o igual a {minimo}.")
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
        # Usamos nuestros helpers para validar precio y stock
        precio = input_float("Precio: ", minimo=0)
        cantidad = input_int("Cantidad inicial: ", minimo=0)

        # Instanciamos la clase y guardamos
        nuevo_producto = Producto(nombre, precio, cantidad)
        inventario.append(nuevo_producto)
        print(f"{nombre} añadido al inventario.")

        if input("¿Desea registrar otro producto? (s/n): ").lower() != "s":
            break


def listar_inventario(inventario):
    print("\nInventario actual:")
    if not inventario:
        print("El inventario está vacío.")
        return
    # Recorremos la lista de objetos y los imprimimos (usa __str__)
    for p in inventario:
        print(p)


def buscar_producto(inventario, prompt):
    # Busca un producto por nombre y retorna la instancia o None
    while True:
        termino = input(prompt).strip()
        if termino.lower() == "salir":
            return None
        
        # Búsqueda simple comparando nombres en minúsculas
        for p in inventario:
            if p.nombre.lower() == termino.lower():
                return p
        
        print("Producto no encontrado, inténtelo de nuevo o escriba 'salir'.")


def actualizar_stock(inventario):
    producto_encontrado = buscar_producto(inventario, "Nombre del producto a actualizar (escribe 'salir' para volver): ")
    if not producto_encontrado:
        return
    
    cantidad_sumar = input_int(f"Cantidad a sumar al stock de {producto_encontrado.nombre}: ", minimo=0)
    producto_encontrado.stock += cantidad_sumar
    print(f"Stock actualizado. Nuevo total: {producto_encontrado.stock}")


def simular_venta(inventario):
    producto_encontrado = buscar_producto(inventario, "Producto que desea vender (escribe 'salir' para volver): ")
    if not producto_encontrado:
        return

    while True:
        cantidad_vender = input_int(f"Cantidad a vender de {producto_encontrado.nombre}: ", minimo=0)
        
        # Verificamos si hay suficiente stock antes de vender
        if cantidad_vender <= producto_encontrado.stock:
            producto_encontrado.stock -= cantidad_vender
            total = cantidad_vender * producto_encontrado.precio
            print(f"Venta realizada. Total a cobrar: ${total:.2f}")
            print(f"Stock restante: {producto_encontrado.stock}")
            return
        
        print(f"No hay suficiente stock (Disponible: {producto_encontrado.stock}). Intente con una cantidad menor.")


def reporte_stock_bajo(inventario, umbral=5):
    # Filtramos los productos que tienen menos stock del permitido
    productos_bajos = list(filter(lambda p: p.stock < umbral, inventario))

    if not productos_bajos:
        print("No hay productos con stock bajo.")
        return

    print(f"\nReporte de productos con stock bajo (menor a {umbral}):")
    for p in productos_bajos:
        print(p)


def main():
    print("Bienvenido a FastStock CLI (Versión 2.0 - POO)")
    inventario = []

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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción incorrecta, inténtelo de nuevo.")


if __name__ == "__main__":
    main()