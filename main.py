#Bienvenida al programa.
print("Bienvenido a FastStock CLI (Gestor de Inventario y Ventas)")

#Lista de diccionarios de productos
inventario = []

#Ciclo para repetir el menú y recibir opciones
salir = False
while not salir:

    #Menú de opciones
    print("Menú principal.")
    print("1. Registrar nuevos productos.")
    print("2. Listar inventario.")
    print("3. Actualizar stock.")
    print("4. Simular venta.")
    print("5. Reporte de stock bajo.")
    print("6. Salir.")

    opcion = input("Por favor, digite la opción que desea: ")

    #Estructuras condicionales para cada opción del menú

    if opcion == "1": #Registrar producto
        aux = False
        while not aux:
            print("Registro de producto.")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad inicial: "))

            #Guardamos la información en un diccionario
            producto = {
                "nombre" : nombre,
                "precio" : precio,
                "stock" : cantidad
            }

            #Agregando el diccionario a la lista
            inventario.append(producto)
            print(f"{nombre} añadido al inventario.")

            respuesta = input("\n¿Desea registrar otro producto? (s/n): ")
            if respuesta != "s":
                aux = True

    elif opcion == "2": #Listar inventario
        print("\nInventario actual.")
        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            for p in inventario:
                print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']}")

    elif opcion == "3": # Actualizar stock
        encontrado = False
        while not encontrado:
            buscar = input("Nombre del producto a actualizar (escribe 'salir' para volver): ")
            
            if buscar.lower() == "salir":
                break # Sale del bucle sin actualizar nada
            
            for p in inventario:
                if p["nombre"].lower() == buscar.lower():
                    nueva_cantidad = int(input(f"Cantidad a sumar al stock de {p['nombre']}: "))
                    p["stock"] += nueva_cantidad
                    print("Stock actualizado.")
                    encontrado = True # Finaliza el bucle while
                    break # Sale del for
            
            if not encontrado:
                print("Producto no encontrado, intentelo de nuevo.")

    elif opcion == "4": # Simular venta
        encontrado = False
        while not encontrado:
            buscar = input("Producto que desea vender (escribe 'salir' para volver): ")
            
            if buscar.lower() == "salir":
                break # Sale del bucle sin vender nada
            
            for p in inventario:
                if p["nombre"].lower() == buscar.lower():
                    cantidad_venta = int(input(f"Cantidad a vender de {p['nombre']}: "))
                    if cantidad_venta <= p["stock"]:
                        p["stock"] -= cantidad_venta
                        total = cantidad_venta * p["precio"]
                        print(f"Venta realizada. Total: ${total}")
                        encontrado = True # Finaliza el bucle while
                    else:
                        print("No hay suficiente stock")
                    break # Sale del for
            
            if not encontrado:
                print("Producto no encontrado, intentelo de nuevo.")

    elif opcion == "5": #Reporte de stock bajo.
        stock_bajo = []
        for p in inventario:
            if p["stock"] < 5:
                stock_bajo.append(p)
        if len(stock_bajo) <= 0:
            print("No hay productos con stock bajo.")
        else:
            print(f"Producto: {p['nombre']} | reporta {p['stock']} unidades.")

    elif opcion == "6": #Salir.
        salir = True

    else: #Validación extra.
        print("Opción incorrecta, inténtelo de nuevo.")