def input_int(prompt, minimo=None):
    # Función auxiliar para asegurar que recibimos un entero válido
    while True:
        try:
            v = int(input(prompt))
            if minimo is not None and v < minimo:
                print(f"Ingrese un número mayor o igual a {minimo}.")
                continue
            return v
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")

def input_float(prompt, minimo=None):
    # Función auxiliar para asegurar que recibimos un precio válido
    while True:
        try:
            v = float(input(prompt))
            if minimo is not None and v < minimo:
                print(f"Ingrese un número mayor o igual a {minimo}.")
                continue
            return v
        except ValueError:
            print("Entrada no válida. Ingrese un número (por ejemplo 12.50).")
