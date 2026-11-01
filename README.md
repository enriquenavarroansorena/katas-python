# 🐍 Katas de Python: 40 ejercicios de lógica

Resolución de las katas del DataProject "Lógica: Katas de Python", con funciones, clases,
excepciones personalizadas y programación funcional (`map`, `filter`, `reduce`, `lambda`).

## 📖 Descripción

Una **kata** es un ejercicio corto de programación pensado para afianzar técnicas mediante la
repetición. Este proyecto recoge 40 de ellas, que van desde manipular cadenas y listas hasta
diseñar clases y gestionar errores.

El objetivo no era solo que cada kata funcionase, sino **entender por qué funciona**: por eso el
código lleva comentarios en los pasos que tienen truco y varias katas incluyen una nota explicando
la decisión tomada cuando el enunciado admitía más de una lectura.

## 🗂 Estructura del proyecto

```
├── katas/
│   ├── katas_python.py   # Las 40 katas resueltas, con su enunciado como comentario
│   └── PruebaKata8.py    # Banco de pruebas de una kata concreta (ver más abajo)
└── README.md
```

### `PruebaKata8.py`

No forma parte de la entrega: es un pequeño archivo de pruebas para comprobar **una kata por
separado** sin ejecutar las 40. Importa las funciones del archivo principal, verifica la lógica con
`assert` y deja preparada la llamada interactiva.

Ese import funciona precisamente porque las demos del archivo principal están dentro de
`if __name__ == "__main__":`: al importarlo, las 40 katas **no** se ejecutan, solo se cargan las
definiciones. Es el patrón que permite que un mismo archivo sea a la vez programa ejecutable y
módulo reutilizable.

## ▶️ Cómo ejecutarlo

Requiere **Python 3.10 o superior** (se ha desarrollado con 3.14) y **no necesita instalar nada**:
solo usa la librería estándar (`functools.reduce` y `math`).

```bash
python katas/katas_python.py
```

> En Windows, si `python` abre la Microsoft Store en lugar de ejecutar el script, usa `py` en su lugar.

El programa ejecuta las 40 demostraciones en orden e imprime el resultado de cada una.

## 🔢 Sobre la numeración

Las katas van de la **1 a la 41**, pero **la 35 no existe**: el enunciado original salta de la 34 a
la 36. Por eso el proyecto contiene **40 ejercicios** y no 41. Se ha respetado la numeración del
enunciado para que cada kata sea fácil de localizar.

## 🧭 Organización del código

Cada kata ocupa una sección con esta forma:

```python
# =============================================================================
# KATA 17
# Enunciado: Crea una función que tome una lista de dígitos y devuelva el número
# correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa reduce()
# =============================================================================
def digitos_a_numero(digitos: list[int]) -> int:
    """Convierte una lista de dígitos en el número entero que representan."""
    # Construcción posicional: en cada paso el acumulado se desplaza una posición
    # a la izquierda (x10) y el nuevo dígito ocupa las unidades.
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)


def demo_17():
    """Caso de uso de la kata 17."""
    print("KATA 17 ->", digitos_a_numero([5, 7, 2]))
```

- **Enunciado literal** como comentario de cabecera, tal y como pide la entrega.
- **Docstring y type hints** en cada función.
- **Comentarios solo donde aportan**: en los pasos sutiles, no en los evidentes.
- Una **función `demo_N()`** por kata, para poder ejecutar y comprobar cada una por separado.
- Un único bloque `if __name__ == "__main__":` al final que lanza las 40 demos.

### Las katas interactivas

Cinco katas (8, 11, 31, 38 y 41) piden datos al usuario con `input()`. En todas ellas se ha separado:

- la **lógica pura**, en una función que recibe los datos ya validados y por tanto se puede probar
  automáticamente;
- la **capa de entrada**, en una función aparte que hace el `input()` y captura los errores.

Gracias a esa separación el archivo se ejecuta entero sin quedarse bloqueado esperando que alguien
teclee, y la parte interactiva sigue disponible poniendo `MODO_INTERACTIVO = True`. Mezclar la
lógica con la entrada y salida habría hecho el código imposible de comprobar.

## 🧠 Decisiones y detalles con miga

Estas son las katas donde el enunciado admitía interpretaciones o donde Python tiene alguna trampa:

| Kata | Detalle |
|---|---|
| **1** | `'A'` y `'a'` se cuentan como la misma letra por defecto, que es lo que se espera al hablar de frecuencia de letras. Un parámetro permite el comportamiento literal |
| **13** | Para eliminar letras repetidas se usa `dict.fromkeys()` en lugar de `set()`: **`set` no garantiza el orden**, así que el resultado variaría entre ejecuciones |
| **17** | `reduce` construye el número posicionalmente: `acumulado * 10 + dígito` |
| **20** | En Python **`True` es un `int`** (`bool` hereda de `int`), así que filtrar por `isinstance(x, int)` colaría los booleanos. Se excluyen con `not isinstance(x, bool)` |
| **22, 23** | `reduce` con valor inicial (1 para el producto, `""` para la concatenación) para que no falle con una lista vacía |
| **27** | Devuelve `0.0` con lista vacía en lugar de provocar un `ZeroDivisionError` |
| **34** | "Retirar la rama de la posición 2" se interpreta como **índice 2** (la tercera rama), por coherencia con `self.ramas[2]`. Queda justificado en un comentario |
| **36** | **Los números del enunciado no cuadran** (ver abajo) |
| **38** | El enunciado no fija los tramos horarios: se usan 6-13 día, 14-20 tarde y el resto noche |
| **41** | El importe final nunca es negativo: un cupón mayor que el precio deja la compra en 0 |

### 🔍 El caso de uso de la kata 36 es imposible tal y como está enunciado

El enunciado pide: crear a Bob con **50 €**, agregarle **20 €** y después transferir **80 €** de Bob
a Alicia. Pero 50 + 20 = **70 €**, así que la transferencia de 80 € no se puede realizar.

En lugar de cambiar los números para que salga, se ha aprovechado como **demostración del manejo de
errores**: el intento de transferir 80 € lanza la excepción, se captura con `try/except` y se muestra
el mensaje; a continuación se hace una transferencia válida de 70 €. El resultado es una clase que
hace lo que debe hacer un sistema bancario de verdad: **negarse a mover dinero que no existe**.

## ✅ Requisitos del proyecto y dónde se demuestran

| Requisito | Katas |
|---|---|
| Tipos de datos básicos y funciones incorporadas | 1, 25, 27, 29 |
| Estructuras de datos y sus métodos | 1, 13, 18, 28, 37 |
| Condicionales | 5, 38, 39, 40, 41 |
| Estructuras de iteración | 1, 28, 32 |
| Funciones (incluidas recursivas y lambdas) | 6 (recursiva), 15, 19, 21, 26, 33 (lambda) |
| **Clases y POO** | **34 (`Arbol`), 36 (`UsuarioBanco`)** |
| Uso de módulos | `functools.reduce` (17, 22, 23, 24) y `math` (40) |
| Manejo de excepciones | 8, 10 (excepción personalizada), 11, 31, 36, 37, 40 |
| Programación funcional | `map` (2, 4, 7, 12, 13) · `filter` (9, 14, 16, 18, 20) · `reduce` (17, 22, 23, 24) |
| Buenas prácticas | Docstrings, type hints, nombres descriptivos, separación lógica/entrada-salida |

## ✒️ Autor

- Enrique Navarro — [@enriquenavarroansorena](https://github.com/enriquenavarroansorena)
