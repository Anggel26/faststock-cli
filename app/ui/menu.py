from app.utils.validators import input_int, input_float

class ConsoleMenu:
    def __init__(self, service):
        self.service = service

    def mostrar_menu(self):
        print("\nMenú principal:")
        print("1. Registrar nuevos productos")
        print("2. Listar inventario")
        print("3. Actualizar stock")
        print("4. Simular venta")
        print("5. Reporte de stock bajo")
        print("6. Salir")

    def registrar_producto(self):
        print("\nRegistro de producto.")
        while True:
            nombre = input("Nombre del producto: ").strip()
            precio = input_float("Precio: ", minimo=0)
            cantidad = input_int("Cantidad inicial: ", minimo=0)

            self.service.agregar_producto(nombre, precio, cantidad)
            print(f"{nombre} añadido al inventario.")

            if input("¿Desea registrar otro producto? (s/n): ").lower() != "s":
                break

    def listar_inventario(self):
        print("\nInventario actual:")
        productos = self.service.obtener_todos()
        if not productos:
            print("El inventario está vacío.")
            return
        
        for p in productos:
            print(p)

    def actualizar_stock(self):
        nombre = input("Nombre del producto a actualizar (escribe 'salir' para volver): ")
        if nombre.lower() == 'salir':
            return

        producto = self.service.buscar_por_nombre(nombre)
        if not producto:
            print("Producto no encontrado.")
            return
        
        cantidad_sumar = input_int(f"Cantidad a sumar al stock de {producto.nombre}: ", minimo=0)
        updated_product = self.service.actualizar_stock(nombre, cantidad_sumar)
        
        if updated_product:
            print(f"Stock actualizado. Nuevo total: {updated_product.stock}")
        else:
            print("Error al actualizar el stock.")

    def simular_venta(self):
        nombre = input("Producto que desea vender (escribe 'salir' para volver): ")
        if nombre.lower() == 'salir':
            return

        while True:
            # Verificamos si existe antes de pedir cantidad
            producto = self.service.buscar_por_nombre(nombre)
            if not producto:
                 print("Producto no encontrado.")
                 return

            cantidad_vender = input_int(f"Cantidad a vender de {producto.nombre}: ", minimo=0)
            
            total, mensaje = self.service.vender_producto(nombre, cantidad_vender)
            
            if total is not None:
                print(mensaje)
                print(f"Stock restante: {producto.stock}")
                return
            else:
                print(mensaje)
                print("Intente con una cantidad menor o escriba 'salir' para cancelar la operación actual.")
                if input("¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                    return

    def reporte_stock_bajo(self):
        productos_bajos = self.service.obtener_stock_bajo()
        if not productos_bajos:
            print("No hay productos con stock bajo.")
            return

        print(f"\nReporte de productos con stock bajo:")
        for p in productos_bajos:
            print(p)

    def iniciar(self):
        print("Bienvenido a FastStock CLI (Versión 3.0 - Arquitectura en Capas)")
        # Cargar datos al inicio
        self.service.repositorio.cargar_todo()

        while True:
            self.mostrar_menu()
            opcion = input("Por favor, digite la opción que desea: ").strip()

            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.listar_inventario()
            elif opcion == "3":
                self.actualizar_stock()
            elif opcion == "4":
                self.simular_venta()
            elif opcion == "5":
                self.reporte_stock_bajo()
            elif opcion == "6":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción incorrecta, inténtelo de nuevo.")
