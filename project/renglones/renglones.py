import random
from project.listado_de_palabras import listado
from project.tablero import rellenar_espacio_palabra


def sacar_value_poner_nuevo(
    arreglo: list, value_palabra: str, datos_palabra: str
) -> bool:
    for i in arreglo:
        if i["respuesta"] == value_palabra[0]:
            i = datos_palabra
    return arreglo



def value_repetido(arreglo: list, value_aleatorio: str) -> bool:
    for i in arreglo:
        if i["respuesta"][0] == value_aleatorio[0]:
            return False
    return True


def horizontales_verticales(
    tablero: list,
    colores: list,
    arreglo_palabras_horizontales: list = [],
    numero_palabra: int = 0,
) -> list:
    caracter_vacio = " "
    bloque_relleno = "\u2587"
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    key_listado = listado.definiciones.keys()
    posicion_aleatoria = random.randint(0, 52)
    key_aleatorio = list(key_listado)[posicion_aleatoria]
    value_listado = listado.definiciones.values()
    value_aleatorio = list(value_listado)[posicion_aleatoria]
    largo_fila = len(tablero[0])
    largo_value_aleatorio = len(value_aleatorio)
    suma = x + (largo_value_aleatorio + 2)
    resta = x - (largo_value_aleatorio + 2)
    largo_palabras_horizontales = len(arreglo_palabras_horizontales)

    if largo_palabras_horizontales == 6:
        numero_palabra = arreglo_palabras_horizontales[-1]["numero_palabra"]
        return verticales(
            tablero, colores, arreglo_palabras_horizontales, numero_palabra
        )

    if value_repetido(arreglo_palabras_horizontales, value_aleatorio):
        datos_palabra = rellenar_espacio_palabra.horizontal_derecho(
            y,
            x,
            suma,
            largo_fila,
            largo_value_aleatorio,
            tablero,
            bloque_relleno,
            value_aleatorio,
            key_aleatorio,
            caracter_vacio,
            numero_palabra,
            colores,
        )
        if not (datos_palabra):
            datos_palabra = rellenar_espacio_palabra.horizontal_izquierdo(
                y,
                x,
                resta,
                largo_value_aleatorio,
                tablero,
                bloque_relleno,
                value_aleatorio,
                key_aleatorio,
                caracter_vacio,
                numero_palabra,
                colores,
            )
            if not (datos_palabra):
                return horizontales_verticales(
                    tablero, colores, arreglo_palabras_horizontales, numero_palabra
                )
            else:
                colores = list(filter(lambda i: i != datos_palabra["color"], colores))
                arreglo_palabras_horizontales.append(datos_palabra)
                numero_palabra = datos_palabra["numero_palabra"]
        else:
            colores = list(filter(lambda i: i != datos_palabra["color"], colores))
            arreglo_palabras_horizontales.append(datos_palabra)
            numero_palabra = datos_palabra["numero_palabra"]
    return horizontales_verticales(
        tablero,
        colores,
        arreglo_palabras_horizontales,
        numero_palabra,
    )


def verticales(
    tablero: list,
    colores,
    arreglo_palabras_horizontales_verticales: list,
    numero_palabra: int,
) -> list:
    bloque_relleno = "\u2587"
    caracter_vacio = " "
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    posicion_aleatoria = random.randint(0, 52)
    key_listado = listado.definiciones.keys()
    key_aleatorio = list(key_listado)[posicion_aleatoria]
    value_listado = listado.definiciones.values()
    value_aleatorio = list(value_listado)[posicion_aleatoria]
    largo_columna = len(tablero) - 1
    largo_value_aleatorio = len(value_aleatorio)
    suma = y + (largo_value_aleatorio + 2)
    resta = y - (largo_value_aleatorio + 2)

    if len(arreglo_palabras_horizontales_verticales) == 12:
        arreglo_completo = arreglo_palabras_horizontales_verticales
        return arreglo_completo
    if value_repetido(arreglo_palabras_horizontales_verticales, value_aleatorio):
        datos_palabra = rellenar_espacio_palabra.vertical_abajo(
            y,
            x,
            suma,
            largo_columna,
            tablero,
            bloque_relleno,
            largo_value_aleatorio,
            value_aleatorio,
            caracter_vacio,
            key_aleatorio,
            numero_palabra,
            colores,
        )
        if not (datos_palabra):
            datos_palabra = rellenar_espacio_palabra.vertical_arriba(
                y,
                x,
                resta,
                tablero,
                bloque_relleno,
                largo_value_aleatorio,
                value_aleatorio,
                caracter_vacio,
                key_aleatorio,
                numero_palabra,
                colores,
            )
            if not (datos_palabra):
                return verticales(
                    tablero,
                    colores,
                    arreglo_palabras_horizontales_verticales,
                    numero_palabra,
                )

            else:
                colores = list(filter(lambda i: i != datos_palabra["color"], colores))
                arreglo_palabras_horizontales_verticales.append(datos_palabra)
                numero_palabra = datos_palabra["numero_palabra"]
        else:
            colores = list(filter(lambda i: i != datos_palabra["color"], colores))
            arreglo_palabras_horizontales_verticales.append(datos_palabra)
            numero_palabra = datos_palabra["numero_palabra"]

    return verticales(
        tablero, colores, arreglo_palabras_horizontales_verticales, numero_palabra
    )
