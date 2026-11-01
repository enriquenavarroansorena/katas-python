"""
PROYECTO LÓGICA: Katas de Python
================================

Resolución de las 40 katas del DataProject de Python del máster en Data Analytics.

Autor   : Enrique Navarro
Python  : 3.14
Ejecutar: py katas/katas_python.py

Nota sobre la numeración
------------------------
Las katas van de la 1 a la 41, pero **la 35 no existe**: el enunciado original salta
de la 34 a la 36. Por eso son 40 ejercicios y no 41.

Organización del archivo
------------------------
Cada kata ocupa una sección encabezada por su enunciado literal y contiene:
  - la función (o clase) que la resuelve, con docstring y type hints;
  - una función `demo_N()` con un caso de uso que imprime el resultado.

Al final, el bloque `if __name__ == "__main__":` ejecuta las 40 demos en orden.

Katas interactivas (8, 11, 31, 38 y 41)
---------------------------------------
Estas katas piden datos por consola. En todas ellas se ha separado la **lógica pura**
(una función que recibe los datos ya validados y por tanto se puede probar) de la
**capa de entrada** (la función que hace el `input()` con su `try/except`).
Así el archivo se ejecuta de principio a fin sin quedarse bloqueado esperando que
alguien teclee, y la parte interactiva sigue disponible para quien quiera usarla:
basta con poner MODO_INTERACTIVO = True.
"""

from functools import reduce
import math

# Si se pone a True, las demos de las katas 8, 11, 31, 38 y 41 piden datos por consola
# en lugar de usar los valores simulados.
MODO_INTERACTIVO = False




# =============================================================================
# KATA 1
# Enunciado: Escribe una función que reciba una cadena de texto como parámetro y
# devuelva un diccionario con las frecuencias de cada letra en la cadena. Los
# espacios no deben ser considerados.
# =============================================================================
def contar_frecuencias(texto: str, ignorar_mayusculas: bool = True) -> dict:
    """Devuelve un diccionario {letra: nº de apariciones} ignorando los espacios."""
    # Decisión de diseño: por defecto 'A' y 'a' se cuentan como la misma letra, que es
    # lo que se suele esperar al hablar de "frecuencia de letras". El parámetro permite
    # el comportamiento literal (distinguir mayúsculas) si se necesitase.
    if ignorar_mayusculas:
        texto = texto.lower()

    frecuencias = {}
    for caracter in texto:
        if caracter == " ":
            continue
        # dict.get(clave, 0) evita tener que comprobar antes si la clave existe
        frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    return frecuencias


def demo_1():
    """Caso de uso de la kata 1."""
    print("KATA 1 ->", contar_frecuencias("data analytics"))
    # Con mayúsculas se aprecia la diferencia entre las dos variantes:
    print("KATA 1 (sin distinguir may/min) ->", contar_frecuencias("Ana"))
    print("KATA 1 (distinguiendo may/min)  ->", contar_frecuencias("Ana", ignorar_mayusculas=False))


# =============================================================================
# KATA 2
# Enunciado: Dada una lista de números, obtén una nueva lista con el doble de
# cada valor. Usa la función map()
# =============================================================================
def duplicar_valores(numeros: list) -> list:
    """Devuelve una lista con cada número multiplicado por dos."""
    # map() devuelve un iterador perezoso: hay que convertirlo a list para verlo
    return list(map(lambda numero: numero * 2, numeros))


def demo_2():
    """Caso de uso de la kata 2."""
    print("KATA 2 ->", duplicar_valores([1, 2, 3, 4, 5]))


# =============================================================================
# KATA 3
# Enunciado: Escribe una función que tome una lista de palabras y una palabra
# objetivo como parámetros. La función debe devolver una lista con todas las
# palabras de la lista original que contengan la palabra objetivo.
# =============================================================================
def buscar_palabras(palabras: list, objetivo: str) -> list:
    """Devuelve las palabras de la lista que contienen la palabra objetivo."""
    # Comparamos en minúsculas para que la búsqueda no dependa de mayúsculas
    objetivo_normalizado = objetivo.lower()
    return [palabra for palabra in palabras if objetivo_normalizado in palabra.lower()]


def demo_3():
    """Caso de uso de la kata 3."""
    lista = ["datos", "database", "analitica", "dataset", "python"]
    print("KATA 3 ->", buscar_palabras(lista, "data"))


# =============================================================================
# KATA 4
# Enunciado: Genera una función que calcule la diferencia entre los valores de
# dos listas. Usa la función map()
# =============================================================================
def restar_listas(primera: list, segunda: list) -> list:
    """Devuelve la resta elemento a elemento de dos listas de números."""
    # map() con dos iterables aplica la lambda en paralelo y se detiene
    # cuando se agota la lista más corta
    return list(map(lambda a, b: a - b, primera, segunda))


def demo_4():
    """Caso de uso de la kata 4."""
    print("KATA 4 ->", restar_listas([10, 20, 30], [1, 2, 3]))


# =============================================================================
# KATA 5
# Enunciado: Escribe una función que tome una lista de números como parámetro y
# un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular
# la media de los números en la lista y determinar si la media es mayor o igual
# que nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, será
# "suspenso". La función debe devolver una tupla que contenga la media y el estado.
# =============================================================================
def calcular_media_y_estado(notas: list, nota_aprobado: float = 5) -> tuple:
    """Devuelve una tupla (media, estado) donde estado es 'aprobado' o 'suspenso'."""
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


def demo_5():
    """Caso de uso de la kata 5."""
    print("KATA 5 ->", calcular_media_y_estado([7, 5, 9, 4]))
    print("KATA 5 ->", calcular_media_y_estado([7, 5, 9, 4], nota_aprobado=7))
    print("KATA 5 ->", calcular_media_y_estado([7, 3, 2, 4]))

# =============================================================================
# KATA 6
# Enunciado: Escribe una función que calcule el factorial de un número de manera
# recursiva.
# =============================================================================
def factorial(numero: int) -> int:
    """Calcula el factorial de un número entero no negativo de forma recursiva."""
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos")
    # Caso base: corta la recursión. 0! y 1! valen 1
    if numero <= 1:
        return 1
    return numero * factorial(numero - 1)


def demo_6():
    """Caso de uso de la kata 6."""
    print("KATA 6 ->", factorial(5))


# =============================================================================
# KATA 7
# Enunciado: Genera una función que convierta una lista de tuplas a una lista de
# strings. Usa la función map()
# =============================================================================
def tuplas_a_strings(tuplas: list, separador: str = " ") -> list:
    """Convierte cada tupla de la lista en una cadena uniendo sus elementos."""
    # str() en cada elemento permite que la tupla mezcle números y textos
    return list(map(lambda tupla: separador.join(map(str, tupla)), tuplas))


def demo_7():
    """Caso de uso de la kata 7."""
    datos = [("Ana", 25), ("Luis", 31), ("Marta", 28)]
    print("KATA 7 ->", tuplas_a_strings(datos, separador=" - "))


# =============================================================================
# KATA 8
# Enunciado: Escribe un programa que pida al usuario dos números e intente
# dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por
# cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un
# mensaje indicando si la división fue exitosa o no.
# =============================================================================
def dividir(dividendo: float, divisor: float) -> float:
    """Divide dos números ya validados y devuelve el resultado."""
    return dividendo / divisor


def pedir_division_interactiva() -> None:
    """Pide dos números por teclado, los divide y gestiona los errores posibles."""
    try:
        dividendo = float(input("Introduce el dividendo: "))
        divisor = float(input("Introduce el divisor: "))
        resultado = dividir(dividendo, divisor)
    except ValueError:
        # float() lanza ValueError cuando el texto no representa un número
        print("División fallida: debes introducir valores numéricos.")
    except ZeroDivisionError:
        print("División fallida: no se puede dividir entre cero.")
    else:
        # El bloque else solo se ejecuta si no hubo ninguna excepción
        print(f"División exitosa: el resultado es {resultado}")


def demo_8():
    """Caso de uso de la kata 8."""
    # En uso real se llamaría a pedir_division_interactiva(), que hace los input().
    # Aquí simulamos los valores ya validados para no bloquear la ejecución.
    print("KATA 8 ->", dividir(10, 4))
    try:
        dividir(10, 0)
    except ZeroDivisionError:
        print("KATA 8 -> División fallida: no se puede dividir entre cero.")


# =============================================================================
# KATA 9
# Enunciado: Escribe una función que tome una lista de nombres de mascotas como
# parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en
# España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente
# Pitón", "Cocodrilo", "Oso"]. Usa la función filter()
# =============================================================================
MASCOTAS_PROHIBIDAS = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]


def filtrar_mascotas_permitidas(mascotas: list) -> list:
    """Devuelve las mascotas que no están en la lista de especies prohibidas."""
    # Normalizamos a minúsculas para que "tigre" y "Tigre" se filtren igual
    prohibidas = [prohibida.lower() for prohibida in MASCOTAS_PROHIBIDAS]
    return list(filter(lambda mascota: mascota.lower() not in prohibidas, mascotas))


def demo_9():
    """Caso de uso de la kata 9."""
    lista = ["Perro", "Tigre", "Gato", "Cocodrilo", "Canario", "Oso"]
    print("KATA 9 ->", filtrar_mascotas_permitidas(lista))


# =============================================================================
# KATA 10
# Enunciado: Escribe una función que reciba una lista de números y calcule su
# promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el
# error adecuadamente.
# =============================================================================
class ListaVaciaError(Exception):
    """Excepción personalizada que se lanza cuando la lista recibida está vacía."""


def calcular_promedio(numeros: list) -> float:
    """Calcula el promedio de una lista; lanza ListaVaciaError si está vacía."""
    if not numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía")
    # reduce() acumula la suma en un solo valor partiendo de 0
    total = reduce(lambda acumulado, numero: acumulado + numero, numeros, 0)
    return total / len(numeros)


def demo_10():
    """Caso de uso de la kata 10."""
    print("KATA 10 ->", calcular_promedio([4, 8, 15, 16, 23, 42]))
    try:
        calcular_promedio([])
    except ListaVaciaError as error:
        print("KATA 10 -> Error capturado:", error)
    
# =============================================================================
# KATA 11
# Enunciado: Escribe un programa que pida al usuario que introduzca su edad. Si
# el usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
# =============================================================================
def validar_edad(edad: int) -> str:
    """Comprueba que la edad esté entre 0 y 120 y devuelve un mensaje de confirmación."""
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años")
    return f"Edad registrada correctamente: {edad} años"


def pedir_edad_interactiva() -> None:
    """Pide la edad por teclado y gestiona texto no numérico o fuera de rango."""
    try:
        # int() lanza ValueError tanto con texto como con decimales ("25.5")
        edad = int(input("Introduce tu edad: "))
        mensaje = validar_edad(edad)
    except ValueError as error:
        print(f"Entrada no válida: {error}")
    else:
        print(mensaje)


def demo_11():
    """Caso de uso de la kata 11."""
    # En uso real se llamaría a pedir_edad_interactiva(), que hace el input().
    print("KATA 11 ->", validar_edad(30))
    try:
        validar_edad(150)
    except ValueError as error:
        print("KATA 11 -> Error capturado:", error)


# =============================================================================
# KATA 12
# Enunciado: Genera una función que al recibir una frase devuelva una lista con
# la longitud de cada palabra. Usa la función map()
# =============================================================================
def longitudes_de_palabras(frase: str) -> list:
    """Devuelve una lista con el número de caracteres de cada palabra de la frase."""
    # split() sin argumentos separa por cualquier espacio y descarta los vacíos
    return list(map(len, frase.split()))


def demo_12():
    """Caso de uso de la kata 12."""
    print("KATA 12 ->", longitudes_de_palabras("Analizamos datos con Python"))


# =============================================================================
# KATA 13
# Enunciado: Genera una función la cual, para un conjunto de caracteres, devuelva
# una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no
# pueden estar repetidas. Usa la función map()
# =============================================================================
def mayusculas_y_minusculas(caracteres: str) -> list:
    """Devuelve una lista de tuplas (mayúscula, minúscula) sin letras repetidas."""
    # set() eliminaría duplicados pero NO conserva el orden de inserción, así que
    # el resultado sería distinto en cada ejecución. dict.fromkeys() sí mantiene
    # el orden de aparición, por lo que la salida es determinista.
    unicos = list(dict.fromkeys(caracteres.lower()))
    return list(map(lambda letra: (letra.upper(), letra.lower()), unicos))


def demo_13():
    """Caso de uso de la kata 13."""
    print("KATA 13 ->", mayusculas_y_minusculas("Analytics"))


# =============================================================================
# KATA 14
# Enunciado: Crea una función que retorne las palabras de una lista de palabras
# que comience con una letra en especifico. Usa la función filter()
# =============================================================================
def filtrar_por_inicial(palabras: list, inicial: str) -> list:
    """Devuelve las palabras de la lista que empiezan por la letra indicada."""
    inicial_normalizada = inicial.lower()
    return list(filter(lambda palabra: palabra.lower().startswith(inicial_normalizada), palabras))


def demo_14():
    """Caso de uso de la kata 14."""
    lista = ["Python", "pandas", "SQL", "PowerBI", "Excel"]
    print("KATA 14 ->", filtrar_por_inicial(lista, "p"))



# =============================================================================
# KATA 15
# Enunciado: Crea una función lambda que sume 3 a cada número de una lista dada.
# =============================================================================
# En código de producción se preferiría un `def` con nombre (más legible y
# depurable), pero aquí el enunciado pide explícitamente una lambda.
sumar_tres = lambda lista: list(map(lambda numero: numero + 3, lista))
sumar_tres.__doc__ = "Devuelve una nueva lista con 3 sumado a cada número."


def demo_15():
    """Caso de uso de la kata 15."""
    print("KATA 15 ->", sumar_tres([1, 2, 3, 10]))


# =============================================================================
# KATA 16
# Enunciado: Escribe una función que tome una cadena de texto y un número entero n
# como parámetros y devuelva una lista de todas las palabras que sean más largas
# que n. Usa la función filter()
# =============================================================================
def palabras_mas_largas_que(texto: str, n: int) -> list[str]:
    """Devuelve las palabras del texto cuya longitud es mayor que n."""
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


def demo_16():
    """Caso de uso de la kata 16."""
    frase = "el analisis de datos requiere practica constante"
    print("KATA 16 ->", palabras_mas_largas_que(frase, 6))


# =============================================================================
# KATA 17
# Enunciado: Crea una función que tome una lista de dígitos y devuelva el número
# correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta
# y dos (572). Usa la función reduce()
# =============================================================================
def digitos_a_numero(digitos: list[int]) -> int:
    """Convierte una lista de dígitos en el número entero que representan."""
    # Construcción posicional: en cada paso el acumulado se desplaza una posición
    # a la izquierda (x10) y el nuevo dígito ocupa las unidades.
    # [5,7,2] -> 5 -> 5*10+7 = 57 -> 57*10+2 = 572
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)


def demo_17():
    """Caso de uso de la kata 17."""
    print("KATA 17 ->", digitos_a_numero([5, 7, 2]))


# =============================================================================
# KATA 18
# Enunciado: Escribe un programa en Python que cree una lista de diccionarios que
# contenga información de estudiantes (nombre, edad, calificación) y use la
# función filter para extraer a los estudiantes con una calificación mayor o
# igual a 90. Usa la función filter()
# =============================================================================
def filtrar_estudiantes_destacados(estudiantes: list[dict], nota_minima: int = 90) -> list[dict]:
    """Devuelve los estudiantes cuya calificación alcanza la nota mínima."""
    return list(filter(lambda estudiante: estudiante["calificacion"] >= nota_minima, estudiantes))


def demo_18():
    """Caso de uso de la kata 18."""
    estudiantes = [
        {"nombre": "Ana", "edad": 22, "calificacion": 95},
        {"nombre": "Luis", "edad": 24, "calificacion": 88},
        {"nombre": "Marta", "edad": 21, "calificacion": 90},
        {"nombre": "Pedro", "edad": 23, "calificacion": 74},
    ]
    destacados = filtrar_estudiantes_destacados(estudiantes)
    print("KATA 18 ->", [estudiante["nombre"] for estudiante in destacados])


# =============================================================================
# KATA 19
# Enunciado: Crea una función lambda que filtre los números impares de una lista dada.
# =============================================================================
# De nuevo, en producción se usaría `def`; aquí se pide lambda de forma explícita.
filtrar_impares = lambda lista: list(filter(lambda numero: numero % 2 != 0, lista))
filtrar_impares.__doc__ = "Devuelve solo los números impares de la lista."


def demo_19():
    """Caso de uso de la kata 19."""
    print("KATA 19 ->", filtrar_impares([1, 2, 3, 4, 5, 6, 7]))


# =============================================================================
# KATA 20
# Enunciado: Para una lista con elementos tipo integer y string obtén una nueva
# lista sólo con los valores int. Usa la función filter()
# =============================================================================
def solo_enteros(elementos: list) -> list[int]:
    """Devuelve únicamente los elementos que son enteros (excluyendo booleanos)."""
    # Detalle sutil: en Python `bool` hereda de `int`, así que isinstance(True, int)
    # es True. Como True/False no son "números" en el sentido del enunciado, los
    # excluimos explícitamente con `not isinstance(elemento, bool)`.
    return list(filter(lambda elemento: isinstance(elemento, int) and not isinstance(elemento, bool), elementos))


def demo_20():
    """Caso de uso de la kata 20."""
    mezcla = [1, "dos", 9, "tres", True, 5, False]
    print("KATA 20 ->", solo_enteros(mezcla))


# =============================================================================
# KATA 21
# Enunciado: Crea una función que calcule el cubo de un número dado mediante una
# función lambda
# =============================================================================
cubo = lambda numero: numero ** 3
cubo.__doc__ = "Devuelve el cubo del número recibido."


def demo_21():
    """Caso de uso de la kata 21."""
    print("KATA 21 ->", cubo(4))


# =============================================================================
# KATA 22
# Enunciado: Dada una lista numérica, obtén el producto total de los valores de
# dicha lista. Usa la función reduce()
# =============================================================================
def producto_total(numeros: list[int | float]) -> int | float:
    """Multiplica todos los valores de la lista y devuelve el resultado."""
    # El valor inicial 1 (elemento neutro del producto) evita el error de reduce()
    # cuando la lista está vacía.
    return reduce(lambda acumulado, numero: acumulado * numero, numeros, 1)


def demo_22():
    """Caso de uso de la kata 22."""
    print("KATA 22 ->", producto_total([1, 2, 3, 4, 5]))


# =============================================================================
# KATA 23
# Enunciado: Concatena una lista de palabras. Usa la función reduce()
# =============================================================================
def concatenar_palabras(palabras: list[str], separador: str = " ") -> str:
    """Concatena todas las palabras de la lista usando un separador."""
    if not palabras:
        return ""
    return reduce(lambda acumulado, palabra: acumulado + separador + palabra, palabras)


def demo_23():
    """Caso de uso de la kata 23."""
    print("KATA 23 ->", concatenar_palabras(["Data", "Analytics", "con", "Python"]))


# =============================================================================
# KATA 24
# Enunciado: Calcula la diferencia total en los valores de una lista. Usa la
# función reduce()
# =============================================================================
def diferencia_total(numeros: list[int | float]) -> int | float:
    """Resta sucesivamente los valores de la lista de izquierda a derecha."""
    # 100 - 20 - 5 - 3 = 72: reduce encadena las restas en orden.
    return reduce(lambda acumulado, numero: acumulado - numero, numeros)


def demo_24():
    """Caso de uso de la kata 24."""
    print("KATA 24 ->", diferencia_total([100, 20, 5, 3]))


# =============================================================================
# KATA 25
# Enunciado: Crea una función que cuente el número de caracteres en una cadena de
# texto dada.
# =============================================================================
def contar_caracteres(texto: str) -> int:
    """Cuenta todos los caracteres de la cadena, espacios incluidos."""
    # El enunciado pide todos los caracteres. Si se quisieran contar solo los
    # caracteres visibles habría que usar len(texto.replace(" ", "")) o
    # sum(1 for c in texto if not c.isspace()).
    return len(texto)


def demo_25():
    """Caso de uso de la kata 25."""
    print("KATA 25 ->", contar_caracteres("Hola mundo"))


# =============================================================================
# KATA 26
# Enunciado: Crea una función lambda que calcule el resto de la división entre dos
# números dados.
# =============================================================================
resto_division = lambda dividendo, divisor: dividendo % divisor
resto_division.__doc__ = "Devuelve el resto de dividir el dividendo entre el divisor."


def demo_26():
    """Caso de uso de la kata 26."""
    print("KATA 26 ->", resto_division(17, 5))


# =============================================================================
# KATA 27
# Enunciado: Crea una función que calcule el promedio de una lista de números.
# =============================================================================
def promedio(numeros: list[int | float]) -> float:
    """Devuelve la media aritmética de la lista; 0.0 si la lista está vacía."""
    # Guardia necesaria: sin ella, una lista vacía provocaría ZeroDivisionError.
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)


def demo_27():
    """Caso de uso de la kata 27."""
    print("KATA 27 ->", promedio([4, 8, 15, 16, 23, 42]))
    print("KATA 27 (lista vacía) ->", promedio([]))

"""Parte C: katas 28 a 41 (la 35 no existe en el enunciado)."""



# =============================================================================
# KATA 28
# Enunciado: Crea una función que busque y devuelva el primer elemento
# duplicado en una lista dada.
# =============================================================================
def primer_duplicado(elementos: list) -> object | None:
    """Devuelve el primer elemento que se repite en la lista, o None si no hay."""
    vistos = set()
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


def demo_28():
    """Caso de uso de la kata 28."""
    print("KATA 28 ->", primer_duplicado([1, 2, 3, 2, 1]))
    # Sin duplicados la función devuelve None, que se muestra con un mensaje claro
    print("KATA 28 (sin duplicados) ->", primer_duplicado(["a", "b", "c"]), "(no hay repetidos)")


# =============================================================================
# KATA 29
# Enunciado: Crea una función que convierta una variable en una cadena de texto
# y enmascare todos los caracteres con el carácter '#', excepto los últimos
# cuatro.
# =============================================================================
def enmascarar(valor: object, visibles: int = 4) -> str:
    """Convierte el valor a texto y oculta con '#' todo menos los últimos caracteres."""
    texto = str(valor)
    # Si el texto es igual o más corto que los visibles, no hay nada que ocultar.
    if len(texto) <= visibles:
        return texto
    return "#" * (len(texto) - visibles) + texto[-visibles:]


def demo_29():
    """Caso de uso de la kata 29."""
    print("KATA 29 ->", enmascarar(4556364607935616))
    print("KATA 29 ->", enmascarar("hola"))


# =============================================================================
# KATA 30
# Enunciado: Crea una función que determine si dos palabras son anagramas, es
# decir, si están formadas por las mismas letras pero en diferente orden.
# =============================================================================
def son_anagramas(palabra_a: str, palabra_b: str) -> bool:
    """Indica si dos palabras contienen exactamente las mismas letras."""
    # Normalizamos: sin mayúsculas ni espacios, para comparar solo las letras.
    limpia_a = sorted(palabra_a.lower().replace(" ", ""))
    limpia_b = sorted(palabra_b.lower().replace(" ", ""))
    return limpia_a == limpia_b


def demo_30():
    """Caso de uso de la kata 30."""
    print("KATA 30 ->", son_anagramas("Roma", "amor"))
    print("KATA 30 ->", son_anagramas("perro", "gato"))


# =============================================================================
# KATA 31
# Enunciado: Crea una función que solicite al usuario ingresar una lista de
# nombres y luego solicite un nombre para buscar en esa lista. Si el nombre
# está en la lista, se imprime un mensaje indicando que fue encontrado, de lo
# contrario, se lanza una excepción.
# =============================================================================
def buscar_nombre(nombres: list[str], buscado: str) -> str:
    """Lógica pura: devuelve un mensaje si el nombre está, si no lanza ValueError."""
    if buscado.strip().lower() not in [nombre.strip().lower() for nombre in nombres]:
        raise ValueError(f"El nombre '{buscado}' no está en la lista.")
    return f"El nombre '{buscado}' fue encontrado en la lista."


def buscar_nombre_interactivo():
    """Pide la lista y el nombre por consola y muestra el resultado de la búsqueda."""
    try:
        entrada = input("Introduce nombres separados por comas: ")
        nombres = [nombre.strip() for nombre in entrada.split(",") if nombre.strip()]
        if not nombres:
            raise ValueError("No has introducido ningún nombre.")
        buscado = input("¿Qué nombre quieres buscar? ")
        print(buscar_nombre(nombres, buscado))
    except ValueError as error:
        print("Error:", error)


def demo_31():
    """Caso de uso de la kata 31."""
    # Simulamos la entrada del usuario; en uso real se llamaría a
    # buscar_nombre_interactivo(), que pide los datos con input().
    nombres = ["Ana", "Luis", "Marta"]
    print("KATA 31 ->", buscar_nombre(nombres, "luis"))
    try:
        buscar_nombre(nombres, "Pedro")
    except ValueError as error:
        print("KATA 31 -> Error capturado:", error)


# =============================================================================
# KATA 32
# Enunciado: Crea una función que tome un nombre completo y una lista de
# empleados, busque el nombre completo en la lista y devuelve el puesto del
# empleado si está en la lista, de lo contrario, devuelve un mensaje indicando
# que la persona no trabaja aquí.
# =============================================================================
def buscar_puesto(nombre_completo: str, empleados: list[dict]) -> str:
    """Devuelve el puesto del empleado buscado o un mensaje si no trabaja aquí."""
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."


def demo_32():
    """Caso de uso de la kata 32."""
    plantilla = [
        {"nombre": "Ana García", "puesto": "Data Analyst"},
        {"nombre": "Luis Pérez", "puesto": "Backend Developer"},
    ]
    print("KATA 32 ->", buscar_puesto("Ana García", plantilla))
    print("KATA 32 ->", buscar_puesto("Pedro Ruiz", plantilla))


# =============================================================================
# KATA 33
# Enunciado: Crea una función lambda que sume elementos correspondientes de dos
# listas dadas.
# =============================================================================
# La lambda recibe dos listas y suma sus elementos posición a posición.
sumar_listas = lambda lista_a, lista_b: list(map(lambda x, y: x + y, lista_a, lista_b))


def demo_33():
    """Caso de uso de la kata 33."""
    print("KATA 33 ->", sumar_listas([1, 2, 3], [10, 20, 30]))


# =============================================================================
# KATA 34
# Enunciado: Crea la clase Arbol, define un árbol genérico con un tronco y
# ramas como atributos. Los métodos disponibles son: crecer_tronco, nueva_rama,
# crecer_ramas, quitar_rama e info_arbol.
# =============================================================================
class Arbol:
    """Árbol genérico con un tronco de cierta longitud y una lista de ramas."""

    def __init__(self):
        """Crea un árbol con tronco de longitud 1 y sin ramas."""
        self.tronco: int = 1
        self.ramas: list[int] = []

    def crecer_tronco(self) -> None:
        """Aumenta en 1 la longitud del tronco."""
        self.tronco += 1

    def nueva_rama(self) -> None:
        """Añade una rama nueva de longitud 1."""
        self.ramas.append(1)

    def crecer_ramas(self) -> None:
        """Aumenta en 1 la longitud de todas las ramas."""
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion: int) -> None:
        """Elimina la rama de la posición indicada (índice de lista, base 0)."""
        if not isinstance(posicion, int) or not 0 <= posicion < len(self.ramas):
            raise IndexError(f"Posición {posicion} no válida: hay {len(self.ramas)} ramas.")
        self.ramas.pop(posicion)

    def info_arbol(self) -> dict:
        """Devuelve el tronco, el número de ramas y las longitudes de las ramas."""
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": list(self.ramas),
        }


def demo_34():
    """Caso de uso de la kata 34."""
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    # Interpretamos "posición 2" como el ÍNDICE 2 (la tercera rama), porque el
    # método recibe un índice de lista y en Python los índices empiezan en 0;
    # así quitar_rama(2) es coherente con self.ramas[2].
    arbol.quitar_rama(2)
    print("KATA 34 ->", arbol.info_arbol())


# =============================================================================
# KATA 36
# Enunciado: Crea la clase UsuarioBanco, representa a un usuario de un banco
# con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos
# para realizar operaciones como retirar dinero, transferir dinero desde otro
# usuario y agregar dinero al saldo.
# =============================================================================
class UsuarioBanco:
    """Usuario de un banco con nombre, saldo y si dispone de cuenta corriente."""

    def __init__(self, nombre: str, saldo: float, cuenta_corriente: bool):
        """Inicializa el usuario con su nombre, saldo inicial y tipo de cuenta."""
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def _validar_cantidad(self, cantidad: float) -> None:
        """Comprueba que la cantidad sea un número positivo."""
        if not isinstance(cantidad, (int, float)) or isinstance(cantidad, bool):
            raise TypeError("La cantidad debe ser un número.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

    def agregar_dinero(self, cantidad: float) -> float:
        """Suma una cantidad al saldo y devuelve el saldo resultante."""
        self._validar_cantidad(cantidad)
        self.saldo += cantidad
        return self.saldo

    def retirar_dinero(self, cantidad: float) -> float:
        """Retira una cantidad del saldo; falla si la cantidad o el saldo no son válidos."""
        self._validar_cantidad(cantidad)
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente ({self.saldo}).")
        self.saldo -= cantidad
        return self.saldo

    def transferir_dinero(self, otro_usuario: "UsuarioBanco", cantidad: float) -> float:
        """Trae dinero DESDE otro usuario hacia este usuario."""
        self._validar_cantidad(cantidad)
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError("El origen debe ser un UsuarioBanco.")
        # Reutilizamos retirar/agregar para que las validaciones de saldo
        # se apliquen una sola vez y en un único sitio.
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)
        return self.saldo

    def __str__(self) -> str:
        """Representación legible del usuario y su saldo."""
        return f"{self.nombre}: {self.saldo} €"


def demo_36():
    """Caso de uso de la kata 36."""
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    print("KATA 36 -> inicio:", alicia, "|", bob)

    bob.agregar_dinero(20)
    print("KATA 36 -> Bob ingresa 20:", alicia, "|", bob)

    # Bob tiene 70 €, así que la transferencia de 80 € del enunciado no es
    # posible: la usamos como caso de error capturado con try/except.
    try:
        alicia.transferir_dinero(bob, 80)
    except ValueError as error:
        print("KATA 36 -> Error capturado:", error)

    # Repetimos la transferencia con una cantidad que Bob sí puede pagar.
    alicia.transferir_dinero(bob, 70)
    print("KATA 36 -> Alicia recibe 70 de Bob:", alicia, "|", bob)

    alicia.retirar_dinero(50)
    print("KATA 36 -> Alicia retira 50:", alicia, "|", bob)

    try:
        alicia.agregar_dinero(-10)
    except ValueError as error:
        print("KATA 36 -> Error capturado:", error)


# =============================================================================
# KATA 37
# Enunciado: Crea una función llamada procesar_texto que procesa un texto según
# la opción especificada: contar_palabras, reemplazar_palabras,
# eliminar_palabra.
# =============================================================================
def contar_palabras(texto: str) -> dict[str, int]:
    """Devuelve un diccionario con el número de apariciones de cada palabra."""
    recuento: dict[str, int] = {}
    for palabra in texto.split():
        recuento[palabra] = recuento.get(palabra, 0) + 1
    return recuento


def reemplazar_palabras(texto: str, palabra_original: str, palabra_nueva: str) -> str:
    """Devuelve el texto con todas las apariciones de una palabra sustituidas."""
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto: str, palabra: str) -> str:
    """Devuelve el texto sin la palabra indicada, respetando un solo espacio."""
    palabras = [p for p in texto.split() if p != palabra]
    return " ".join(palabras)


def procesar_texto(texto: str, opcion: str, *args) -> object:
    """Aplica al texto la operación elegida: 'contar', 'reemplazar' o 'eliminar'."""
    operaciones = {
        "contar": contar_palabras,
        "reemplazar": reemplazar_palabras,
        "eliminar": eliminar_palabra,
    }
    if opcion not in operaciones:
        raise ValueError(
            f"Opción '{opcion}' no válida. Usa: {', '.join(operaciones)}."
        )
    # Los *args son los parámetros extra que necesita cada operación concreta.
    return operaciones[opcion](texto, *args)


def demo_37():
    """Caso de uso de la kata 37."""
    texto = "el gato y el perro y el pez"
    print("KATA 37 ->", procesar_texto(texto, "contar"))
    print("KATA 37 ->", procesar_texto(texto, "reemplazar", "gato", "loro"))
    print("KATA 37 ->", procesar_texto(texto, "eliminar", "el"))
    try:
        procesar_texto(texto, "ordenar")
    except ValueError as error:
        print("KATA 37 -> Error capturado:", error)


# =============================================================================
# KATA 38
# Enunciado: Genera un programa que nos diga si es de noche, de día o tarde
# según la hora proporcionada por el usuario.
# =============================================================================
def momento_del_dia(hora: int) -> str:
    """Clasifica una hora (0-23) como mañana, tarde o noche."""
    if not 0 <= hora <= 23:
        raise ValueError("La hora debe estar entre 0 y 23.")
    if 6 <= hora < 14:
        return "Es de día (mañana)."
    if 14 <= hora < 21:
        return "Es por la tarde."
    return "Es de noche."


def momento_del_dia_interactivo():
    """Pide la hora por consola y muestra si es de día, tarde o noche."""
    try:
        hora = int(input("¿Qué hora es? (0-23): "))
        print(momento_del_dia(hora))
    except ValueError as error:
        print("Error:", error if str(error).startswith("La hora") else "Introduce un número entero.")


def demo_38():
    """Caso de uso de la kata 38."""
    # Simulamos varias horas; en uso real se llamaría a momento_del_dia_interactivo().
    for hora in (9, 17, 23):
        print(f"KATA 38 -> {hora}h:", momento_del_dia(hora))


# =============================================================================
# KATA 39
# Enunciado: Escribe un programa que determine qué calificación en texto tiene
# un alumno en base a su calificación numérica. Las reglas son: 0-69
# insuficiente, 70-79 bien, 80-89 muy bien, 90-100 excelente.
# =============================================================================
def calificacion_texto(nota: float) -> str:
    """Traduce una nota numérica (0-100) a su calificación en texto."""
    if not 0 <= nota <= 100:
        raise ValueError("La nota debe estar entre 0 y 100.")
    if nota < 70:
        return "insuficiente"
    if nota < 80:
        return "bien"
    if nota < 90:
        return "muy bien"
    return "excelente"


def demo_39():
    """Caso de uso de la kata 39."""
    for nota in (45, 72, 85, 97):
        print(f"KATA 39 -> {nota}:", calificacion_texto(nota))


# =============================================================================
# KATA 40
# Enunciado: Escribe una función que tome dos parámetros: figura (una cadena
# que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con
# los datos necesarios para calcular el área de la figura).
# =============================================================================
def calcular_area(figura: str, datos: tuple) -> float:
    """Calcula el área de un rectángulo, círculo o triángulo a partir de sus datos."""
    # Cada figura guarda cuántos datos necesita y cómo calcular su área.
    formulas = {
        "rectangulo": (2, lambda base, altura: base * altura),
        "circulo": (1, lambda radio: math.pi * radio ** 2),
        "triangulo": (2, lambda base, altura: (base * altura) / 2),
    }
    if figura not in formulas:
        raise ValueError(f"Figura '{figura}' no válida. Usa: {', '.join(formulas)}.")

    n_datos, formula = formulas[figura]
    if len(datos) != n_datos:
        raise ValueError(f"'{figura}' necesita {n_datos} dato(s) y has dado {len(datos)}.")
    if any(dato <= 0 for dato in datos):
        raise ValueError("Todos los datos deben ser mayores que cero.")
    return formula(*datos)


def demo_40():
    """Caso de uso de la kata 40."""
    print("KATA 40 -> rectángulo(4, 5):", calcular_area("rectangulo", (4, 5)))
    print("KATA 40 -> círculo(3):", round(calcular_area("circulo", (3,)), 2))
    print("KATA 40 -> triángulo(6, 4):", calcular_area("triangulo", (6, 4)))
    try:
        calcular_area("rombo", (2, 3))
    except ValueError as error:
        print("KATA 40 -> Error capturado:", error)


# =============================================================================
# KATA 41
# Enunciado: Programa que utilice condicionales para determinar el monto final
# de una compra tras aplicar un descuento: pide el precio original, pregunta si
# tiene cupón (sí/no), si dice que sí pide el valor del cupón, lo aplica si es
# válido (mayor que cero) y muestra el precio final.
# =============================================================================
def aplicar_cupon(precio: float, cupon: float = 0.0) -> float:
    """Resta el cupón al precio si es válido; el resultado nunca baja de 0."""
    if precio <= 0:
        raise ValueError("El precio original debe ser mayor que cero.")
    if cupon <= 0:
        return precio
    # Un cupón mayor que el precio deja la compra en 0, no en negativo.
    return max(precio - cupon, 0.0)


def aplicar_cupon_interactivo():
    """Pide precio y cupón por consola y muestra el precio final de la compra."""
    try:
        precio = float(input("Precio original: "))
        respuesta = input("¿Tienes cupón de descuento? (sí/no): ").strip().lower()
        cupon = 0.0
        if respuesta in ("si", "sí", "s"):
            cupon = float(input("Valor del cupón: "))
            if cupon <= 0:
                print("El cupón no es válido, no se aplica descuento.")
        print(f"Precio final: {aplicar_cupon(precio, cupon):.2f} €")
    except ValueError as error:
        print("Error:", error if str(error).startswith("El precio") else "Introduce un número válido.")


def demo_41():
    """Caso de uso de la kata 41."""
    # Simulamos las respuestas del usuario; en uso real se llamaría a
    # aplicar_cupon_interactivo(), que pide los datos con input().
    print("KATA 41 -> 100 € con cupón de 15 €:", aplicar_cupon(100, 15))
    print("KATA 41 -> 100 € sin cupón:", aplicar_cupon(100, 0))
    print("KATA 41 -> 20 € con cupón de 50 €:", aplicar_cupon(20, 50))


# =============================================================================
# EJECUCIÓN DE TODAS LAS KATAS
# =============================================================================
# Este bloque solo se ejecuta cuando el archivo se lanza directamente
# (py katas/katas_python.py). Si el archivo se importase desde otro módulo,
# las demos no se dispararían: es la utilidad de `if __name__ == "__main__"`.
if __name__ == "__main__":
    # La kata 35 no existe en el enunciado original (salta de la 34 a la 36).
    demos = [
        demo_1, demo_2, demo_3, demo_4, demo_5, demo_6, demo_7, demo_8, demo_9, demo_10,
        demo_11, demo_12, demo_13, demo_14, demo_15, demo_16, demo_17, demo_18, demo_19, demo_20,
        demo_21, demo_22, demo_23, demo_24, demo_25, demo_26, demo_27, demo_28, demo_29, demo_30,
        demo_31, demo_32, demo_33, demo_34, demo_36, demo_37, demo_38, demo_39, demo_40, demo_41,
    ]

    print("=" * 79)
    print("PROYECTO LÓGICA: KATAS DE PYTHON".center(79))
    print("=" * 79)

    for demo in demos:
        print()
        demo()

    print()
    print("=" * 79)
    print(f"{len(demos)} katas ejecutadas correctamente.".center(79))
    print("=" * 79)
