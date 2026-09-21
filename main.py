"""
Nombre: Valdez Curiel Diana
Matrícula: 2403230163
Asignatura: Ciencia de Datos
Fecha: 21/09/2026
"""

from procesador import extraer_parametros
from funciones import evaluar_funcion


def capturar_funcion():
    # Capturar la función
    while True:
        try:
            expresion = input("Ingresa la función lineal: ")

            m, b = extraer_parametros(expresion)

            print("\nFunción capturada.")
            print(f"Pendiente (m): {m}")
            print(f"Ordenada al origen (b): {b}")

            return m, b

        except ValueError:
            print("Error: función no válida.")
            print("Ejemplos: 2x + 3, -1.5x - 4, x + 5")


def capturar_muestras():
    # Capturar cantidad de muestras
    while True:
        try:
            n = int(input("Ingresa el número de muestras: "))

            if n > 0:
                return n

            print("El número debe ser mayor que 0.")

        except ValueError:
            print("Error: ingresa un número entero.")


def capturar_valores(m, b, n):
    # Capturar valores de x
    resultados = []

    for i in range(1, n + 1):
        while True:
            try:
                x = float(input(f"Ingresa x{i}: "))

                # Calcular y
                y = evaluar_funcion(m, b, x)

                resultados.append((x, y))
                break

            except ValueError:
                print("Error: ingresa un número válido.")

    # Mostrar resultados
    print("\n--- RESULTADOS ---")
    print(f"{'x':>10} {'y':>10}")
    print("-" * 21)

    for x, y in resultados:
        print(f"{x:>10.2f} {y:>10.2f}")


def mostrar_menu():
    # Mostrar menú
    print("\n--- MENU PRINCIPAL ---")
    print("1. Capturar función lineal")
    print("2. Capturar número de muestras (n)")
    print("3. Capturar valores de x y evaluar")
    print("4. Salir")


def main():
    # Guardar datos
    m = None
    b = None
    n = None

    # Mantener el menú activo
    while True:
        mostrar_menu()

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            m, b = capturar_funcion()

        elif opcion == "2":
            n = capturar_muestras()
            print(f"Número de muestras: {n}")

        elif opcion == "3":
            if m is None or b is None:
                print("Primero captura la función.")

            elif n is None:
                print("Primero captura el número de muestras.")

            else:
                print(f"\nFunción: y = {m}x + {b}")
                capturar_valores(m, b, n)

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()