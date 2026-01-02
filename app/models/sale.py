import datetime
import uuid

class Venta:
    # Representa una transacción de venta
    def __init__(self, producto_nombre, cantidad, precio_unitario, costo_unitario, fecha=None):
        self.id = str(uuid.uuid4())[:8] # ID corto único
        self.producto_nombre = producto_nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.costo_unitario = costo_unitario
        self.fecha = fecha if fecha else datetime.datetime.now()
        
        # Cálculos automáticos
        self.total = self.precio_unitario * self.cantidad
        self.ganancia = (self.precio_unitario - self.costo_unitario) * self.cantidad

    def __str__(self):
        return f"[{self.fecha.strftime('%Y-%m-%d %H:%M')}] {self.cantidad}x {self.producto_nombre} | Total: ${self.total:.2f} (Ganancia: ${self.ganancia:.2f})"
