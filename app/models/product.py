import datetime

class Producto:
    # Definimos la estructura básica de nuestro producto
    def __init__(self, nombre, precio, stock, fecha_registro=None, costo=0.0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.fecha_registro = fecha_registro if fecha_registro else datetime.datetime.now()
        self.costo = costo

    # Método para mostrar el producto de forma legible
    def __str__(self):
        margen = self.precio - self.costo
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Costo: ${self.costo:.2f} | Margen: ${margen:.2f} | Stock: {self.stock} | Fecha: {self.fecha_registro.strftime('%Y-%m-%d %H:%M')}"
