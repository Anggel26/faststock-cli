import os
import datetime
from app.models.product import Producto

class InventoryRepository:
    # Clase para manejar la persistencia del inventario
    def __init__(self, nombre_archivo):
        #Normalizamos la ruta del archivo
        self.nombre_archivo = nombre_archivo
        self.productos = []

    def guardar_todo(self):
        with open(encoding="utf-8", file=self.nombre_archivo, mode="w") as archivo:
            # Guardamos cada producto en una línea separando campos con ;
            # Ahora incluimos el costo al final
            for p in self.productos:
                linea = f"{p.nombre};{p.precio};{p.stock};{p.fecha_registro.isoformat()};{p.costo}\n"
                archivo.write(linea)

    def cargar_todo(self):
        self.productos = []
        if not os.path.exists(self.nombre_archivo):
            return
        
        with open(encoding="utf-8", file=self.nombre_archivo, mode="r") as archivo:
            for linea in archivo:
                linea = linea.strip() # Limpiamos espacios y saltos
                if not linea:         # Si quedó vacía, saltamos
                    continue
                
                partes = linea.split(";") 
                
                # Verificamos si tenemos los campos necesarios (versión nueva con costo o vieja sin costo)
                if len(partes) >= 4:
                    try:
                        nombre = partes[0]
                        precio = float(partes[1])
                        stock = int(partes[2])
                        fecha_str = partes[3]
                        
                        # Intentamos leer el costo si existe, si no asumimos 0.0 (migración)
                        costo = 0.0
                        if len(partes) > 4:
                            costo = float(partes[4])

                        fecha_registro = datetime.datetime.fromisoformat(fecha_str)
                        producto = Producto(nombre, precio, stock, fecha_registro, costo)
                        self.productos.append(producto)
                    except Exception as e:
                        print(f"Error cargando línea '{linea}': {e}")
                else:
                    print(f"Línea ignorada (formato incorrecto): {linea}")
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_todo()

    def buscar_producto_por_nombre(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                return p
        return None
