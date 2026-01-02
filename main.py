"""FastStock CLI - Gestor de inventario y ventas (Versión Persistencia y Auditoría)."""
from app.repositories.inventory import InventoryRepository
from app.services.manager import InventoryService
from app.ui.menu import ConsoleMenu

def main():
    # Inicialización de dependencias
    repository = InventoryRepository("data/inventario.txt")
    service = InventoryService(repository)
    menu = ConsoleMenu(service)
    
    # Iniciar aplicación
    menu.iniciar()

if __name__ == "__main__":
    main()