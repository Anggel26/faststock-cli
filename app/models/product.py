import datetime

class Producto:
    # Definimos la estructura básica de nuestro producto
    def __init__(self, nombre, precio, stock, fecha_registro=None):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.fecha_registro = fecha_registro if fecha_registro else datetime.datetime.now()

    # Método para mostrar el producto de forma legible
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} | Fecha de registro: {self.fecha_registro.strftime('%Y-%m-%d %H:%M')}"
