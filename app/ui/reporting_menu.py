from app.utils.validators import input_int
from app.services.reporting_service import ReportingService

class ReportingMenu:
    def __init__(self, service):
        # Recibimos InventoryService para acceder al repo de ventas
        # O idealmente recibir ReportingService directamente.
        # Vamos a instanciar ReportingService aquí usando el repo del inventory service
        self.reporting_service = ReportingService(service.sales_repository)

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Reportes y Análisis ---")
            print("1. Reporte de Ventas de Hoy")
            print("2. Reporte Mensual")
            print("3. Exportar Datos")
            print("4. Volver al menú principal")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.mostrar_reporte(self.reporting_service.reporte_ventas_hoy())
            elif opcion == "2":
                self.reporte_mensual()
            elif opcion == "3":
                self.exportar()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    def mostrar_reporte(self, datos):
        print(f"\nResultados: {datos['titulo']}")
        print(f"Transacciones: {datos['transacciones']}")
        print(f"Ítems vendidos: {datos['items_vendidos']}")
        print(f"Ingresos Totales: ${datos['total_ingresos']:.2f}")
        print(f"Ganancia Neta:    ${datos['total_ganancias']:.2f}")
        print("-" * 30)
        
        if datos['transacciones'] > 0:
            mostrar_detalle = input("¿Ver detalle de transacciones? (s/n): ").lower()
            if mostrar_detalle == 's':
                print("\nDetalle:")
                for v in datos['detalle']:
                    print(v)

    def reporte_mensual(self):
        print("\nGenerar reporte mensual")
        mes = input_int("Mes (1-12) [Dejar vacío para mes actual]: ", opcional=True)
        anio = input_int("Año [Dejar vacío para año actual]: ", opcional=True)
        
        datos = self.reporting_service.reporte_ventas_mensual(mes, anio)
        self.mostrar_reporte(datos)

    def exportar(self):
        print("\nExportando datos...")
        # Por defecto exportamos todo el histórico disponible en el repo
        todas_las_ventas = self.reporting_service.sales_repository.ventas
        if not todas_las_ventas:
            print("No hay datos para exportar.")
            return

        nombre = input("Nombre del archivo (default: reporte_sales.csv): ").strip()
        if not nombre: nombre = "reporte_sales.csv"
        
        msg = self.reporting_service.exportar_csv(todas_las_ventas, nombre)
        print(msg)
