"""
Prueba manual de la KATA 8 (división con manejo de excepciones).

Este archivo NO forma parte de la entrega: es un banco de pruebas para comprobar
la kata por separado, sin tener que ejecutar las 40.

Ejecutar:  py katas/PruebaKata8.py
"""

# Importamos las dos funciones desde el archivo principal.
# Esto funciona porque en katas_python.py las demos están dentro de
# `if __name__ == "__main__":`, así que al importarlo NO se ejecutan las 40 katas:
# solo se cargan las definiciones de funciones.
from katas_python import dividir, pedir_division_interactiva


def pruebas_automaticas() -> None:
    """Comprueba la lógica pura sin necesidad de teclado."""
    print("--- Pruebas automáticas ---")

    # Caso normal
    print("10 / 4 =", dividir(10, 4))          # esperado: 2.5
    print("9 / 3  =", dividir(9, 3))           # esperado: 3.0
    print("7 / 2  =", dividir(7, 2))           # esperado: 3.5

    # Caso de error: división por cero
    try:
        dividir(10, 0)
        print("ERROR: debería haber lanzado ZeroDivisionError")
    except ZeroDivisionError:
        print("10 / 0 -> ZeroDivisionError capturado correctamente ✔")

    # Comprobación automática con assert: si la condición es falsa, el programa
    # se detiene con AssertionError. Es la forma más simple de "testear".
    assert dividir(10, 4) == 2.5
    assert dividir(9, 3) == 3.0
    print("Todos los assert han pasado ✔")


if __name__ == "__main__":
    pruebas_automaticas()

    # Prueba interactiva: descomenta la línea de abajo para probar los input().
    # Valores sugeridos para ver los tres caminos:
    #   10 y 4    -> división exitosa
    #   10 y 0    -> ZeroDivisionError
    #   hola y 4  -> ValueError
    # pedir_division_interactiva()
