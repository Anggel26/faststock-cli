from app.models.product import Producto
from app.models.sale import Venta
from app.repositories.sales_repository import SalesRepository

class InventoryService:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.sales_repository = SalesRepository("data/ventas.txt") # Inicializamos el repo de ventas interno
        self.sales_repository.cargar_historico()

    # Registra un nuevo producto y lo guarda
    def agregar_producto(self, nombre, precio, stock, costo=0.0):
        if self.buscar_por_nombre(nombre):
            return None
            
        producto = Producto(nombre, precio, stock, costo=costo)
        self.repositorio.agregar_producto(producto)
        return producto

    # Devuelve la lista completa del inventario
    def obtener_todos(self):
        return self.repositorio.productos

    # Busca un producto por su nombre exacto
    def buscar_por_nombre(self, nombre):
        return self.repositorio.buscar_producto_por_nombre(nombre)

    # Suma cantidad al stock existente
    def actualizar_stock(self, nombre_producto, cantidad_sumar):
        producto = self.buscar_por_nombre(nombre_producto)
        if producto:
            producto.stock += cantidad_sumar
            self.repositorio.guardar_todo()
            return producto
        return None

    # Actualiza el costo de un producto
    def actualizar_costo(self, nombre_producto, nuevo_costo):
        producto = self.buscar_por_nombre(nombre_producto)
        if producto:
            producto.costo = nuevo_costo
            self.repositorio.guardar_todo()
            return producto
        return None

    # Procesa una venta si hay suficiente stock
    def vender_producto(self, nombre_producto, cantidad_vender):
        producto = self.buscar_por_nombre(nombre_producto)
        if not producto:
            return None, "Producto no encontrado."
        
        if cantidad_vender > producto.stock:
            return None, f"No hay suficiente stock (Disponible: {producto.stock})."
        
        producto.stock -= cantidad_vender
        
        # Registramos la venta
        # Usamos el costo actual del producto para el historial
        nueva_venta = Venta(producto.nombre, cantidad_vender, producto.precio, producto.costo)
        self.sales_repository.guardar_venta(nueva_venta)
        
        total = nueva_venta.total
        self.repositorio.guardar_todo()
        return total, f"Venta realizada. Total: ${total:.2f} (Ganancia: ${nueva_venta.ganancia:.2f})"

    # Filtra los productos con poco stock
    def obtener_stock_bajo(self, umbral=5):
        return list(filter(lambda p: p.stock < umbral, self.repositorio.productos))
