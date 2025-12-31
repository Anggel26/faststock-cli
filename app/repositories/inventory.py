import os
import datetime
from app.models.product import Producto

class InventoryRepository:
    # Clase para manejar la persistencia del inventario
    def __init__(self, nombre_archivo):
        #Normalizamos la ruta del archivo
        # Assuming the file is stored relative to the project root or a specific data dir
        # For now, keeping it simple relative to where main.py runs or absolute path
        # Adjusting to likely be in the root or data folder. 
        # Since main.py is in root, looking for file in root is fine.
        self.nombre_archivo = nombre_archivo
        self.productos = []

    def guardar_todo(self):
        with open(encoding="utf-8", file=self.nombre_archivo, mode="w") as archivo:
            # Guardamos cada producto en una línea del archivo separando campos con ;
            for p in self.productos:
                linea = f"{p.nombre};{p.precio};{p.stock};{p.fecha_registro.isoformat()}\n"
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
                
                # Verificamos si tenemos todos los campos necesarios
                if len(partes) == 4:
                    nombre, precio, stock, fecha_str = partes
                    fecha_registro = datetime.datetime.fromisoformat(fecha_str)
                    producto = Producto(nombre, float(precio), int(stock), fecha_registro)
                    self.productos.append(producto)
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_todo()

    def buscar_producto_por_nombre(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                return p
        return None
