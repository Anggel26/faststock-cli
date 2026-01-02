import os
import datetime
from app.models.sale import Venta

class SalesRepository:
    # Clase encargada del historial de ventas
    def __init__(self, nombre_archivo="ventas.txt"):
        self.nombre_archivo = nombre_archivo
        self.ventas = []

    def guardar_venta(self, venta):
        self.ventas.append(venta)
        # Modo 'a' (append) para agregar al final sin borrar lo anterior
        with open(encoding="utf-8", file=self.nombre_archivo, mode="a") as archivo:
            # Formato: ID;PRODUCTO;CANTIDAD;PRECIO;COSTO;TOTAL;GANANCIA;FECHA
            linea = f"{venta.id};{venta.producto_nombre};{venta.cantidad};{venta.precio_unitario};{venta.costo_unitario};{venta.total};{venta.ganancia};{venta.fecha.isoformat()}\n"
            archivo.write(linea)

    def cargar_historico(self):
        self.ventas = []
        if not os.path.exists(self.nombre_archivo):
            return

        with open(encoding="utf-8", file=self.nombre_archivo, mode="r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea: continue

                partes = linea.split(";")
                if len(partes) >= 8:
                    # Recuperamos los datos
                    uid, prod, cant, precio, costo, total, ganancia, fecha_str = partes
                    
                    # Reconstruimos el objeto Venta
                    venta = Venta(prod, int(cant), float(precio), float(costo))
                    # Sobrescribimos fecha y ID originales
                    venta.id = uid
                    venta.fecha = datetime.datetime.fromisoformat(fecha_str)
                    
                    self.ventas.append(venta)

    def obtener_ventas_rango(self, fecha_inicio, fecha_fin):
        # Filtramos ventas dentro de un rango de fechas
        resultado = []
        for v in self.ventas:
            if fecha_inicio <= v.fecha <= fecha_fin:
                resultado.append(v)
        return resultado
