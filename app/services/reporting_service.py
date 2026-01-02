import datetime

class ReportingService:
    # Servicio dedicado a la generación de reportes y análisis
    def __init__(self, sales_repository):
        self.sales_repository = sales_repository

    def reporte_ventas_hoy(self):
        hoy = datetime.datetime.now().date()
        inicio = datetime.datetime(hoy.year, hoy.month, hoy.day, 0, 0, 0)
        fin = datetime.datetime(hoy.year, hoy.month, hoy.day, 23, 59, 59)
        
        ventas_hoy = self.sales_repository.obtener_ventas_rango(inicio, fin)
        return self._generar_resumen(ventas_hoy, f"Reporte del {hoy}")

    def reporte_ventas_mensual(self, mes=None, anio=None):
        fecha_actual = datetime.datetime.now()
        mes = mes if mes else fecha_actual.month
        anio = anio if anio else fecha_actual.year
        
        # Definir rango del mes
        inicio = datetime.datetime(anio, mes, 1, 0, 0, 0)
        # Truco simple para fin de mes: primer día del mes siguiente - 1 segundo
        if mes == 12:
            fin = datetime.datetime(anio + 1, 1, 1, 0, 0, 0) - datetime.timedelta(seconds=1)
        else:
            fin = datetime.datetime(anio, mes + 1, 1, 0, 0, 0) - datetime.timedelta(seconds=1)

        ventas_mes = self.sales_repository.obtener_ventas_rango(inicio, fin)
        return self._generar_resumen(ventas_mes, f"Reporte Mensual ({mes}/{anio})")

    def _generar_resumen(self, lista_ventas, titulo):
        total_ingresos = sum(v.total for v in lista_ventas)
        total_ganancias = sum(v.ganancia for v in lista_ventas)
        cantidad_total = len(lista_ventas)
        productos_vendidos = sum(v.cantidad for v in lista_ventas)
        
        return {
            "titulo": titulo,
            "total_ingresos": total_ingresos,
            "total_ganancias": total_ganancias,
            "transacciones": cantidad_total,
            "items_vendidos": productos_vendidos,
            "detalle": lista_ventas
        }

    def exportar_csv(self, lista_ventas, nombre_archivo="reporte_exportado.csv"):
        # Exporta una lista de ventas a CSV manualmente
        header = "ID,Fecha,Producto,Cantidad,Precio Unitario,Costo Unitario,Total,Ganancia\n"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(header)
            for v in lista_ventas:
                linea = f"{v.id},{v.fecha},{v.producto_nombre},{v.cantidad},{v.precio_unitario},{v.costo_unitario},{v.total},{v.ganancia}\n"
                f.write(linea)
        return f"Reporte exportado a {nombre_archivo}"
