import random


# def orientacion_palabra(range_palabra, range_orientacion, contador):
#     if range_palabra <= range_orientacion:
#         if contador < 3:
#             tipo_de_palabra = "horizontal derecho"
#         elif 3 <= contador < 6:
#             tipo_de_palabra = "vertical abajo"

#     elif range_palabra >= 0:
#         if 6 <= contador < 9:
#             tipo_de_palabra = "horizontal izquierdo"
#         elif 9 <= contador < 12:
#             tipo_de_palabra = "vertical arriba"

#     return tipo_de_palabra


# def colocar_palabra(
#     y,
#     x,
#     orientacion,
#     value_nuevo,
#     length_value,
#     tablero,
#     bloque_relleno,
#     caracter_vacio,
# ):
#     for j in range(length_value + 2):
#         if j == 0 or j == value_nuevo + 1:
#             if orientacion == "horizontal derecho":
#                 tablero[y][x + j] = bloque_relleno
#             elif orientacion == "vertical abajo":
#                 tablero[y + j][x] = bloque_relleno

#             elif orientacion == "horizontal izquierdo":
#                 tablero[y][x - j] = bloque_relleno

#             elif orientacion == "vertical arriba":
#                 tablero[y - j][x] = bloque_relleno

#         elif j == 1:
#             if orientacion == "horizontal derecho":
#                 tablero[y][x + j] = value_nuevo[0]
#             elif orientacion == "vertical abajo":
#                 tablero[y + j][x] = value_nuevo[0]

#             elif orientacion == "horizontal izquierdo":
#                 tablero[y][x - j] = value_nuevo[0]

#             elif orientacion == "vertical arriba":
#                 tablero[y - j][x] = value_nuevo[0]

#         else:
#             if orientacion == "horizontal derecho":
#                 tablero[y][x + j] = caracter_vacio
#             elif orientacion == "vertical abajo":
#                 tablero[y + j][x] = caracter_vacio

#             elif orientacion == "horizontal izquierdo":
#                 tablero[y][x - j] = caracter_vacio

#             elif orientacion == "vertical arriba":
#                 tablero[y - j][x] = caracter_vacio

#     return None


# def verificar_espacio_vacio(y, x, orientacion, length_value, tablero):
#     if orientacion == "horizontal derecho":
#         espacios = sum(1 for i in range(length_value + 2) if not tablero[y][x + i])

#     elif orientacion == "vertical abajo":
#         espacios = sum(1 for i in range(length_value + 2) if not tablero[y + i][x])

#     elif orientacion == "horizontal izquierdo":
#         espacios = sum(1 for i in range(length_value + 2) if not tablero[y][x - i])

#     elif orientacion == "vertical arriba":
#         espacios = sum(1 for i in range(length_value + 2) if not tablero[y - i][x])

#     if espacios == length_value + 2:
#         return True

#     else:
#         return False


# def rellenar_palabra(
#     y: int,
#     x: int,
#     range_palabra: int,
#     range_orientacion: int,
#     tablero: list,
#     key_nuevo: str,
#     value_nuevo: str,
#     colores: list,
#     contador: int = 0,
# ):
#     orientacion = orientacion_palabra(range_palabra, range_orientacion, contador)
#     length_value = len(value_nuevo)
#     bloque_relleno = "\u2587"
#     caracter_vacio = ""

#     verificacion = verificar_espacio_vacio()

#     if verificacion:
#         colocar_palabra(
#             y,
#             x,
#             orientacion,
#             value_nuevo,
#             length_value,
#             tablero,
#             bloque_relleno,
#             caracter_vacio,
#         )
#         color_aleatorio = random.randint(0, len(colores) - 1)
#         color = colores[color_aleatorio]
#         datos_palabra = {
#             "numero_palabra": contador,
#             "fila": y,
#             "columna": x + 1,
#             "acertijo": key_nuevo,
#             "respuesta": value_nuevo,
#             "orientacion": orientacion,
#             "color": color,
#         }
#         return datos_palabra

#     else:
#         return None


def horizontal_derecho(
    y: int,
    x: int,
    suma: int,
    largo_fila: int,
    largo_value_aleatorio: int,
    tablero: list,
    bloque_relleno: str,
    value_aleatorio: str,
    key_aleatorio: str,
    caracter_vacio: str,
    numero_palabra: int,
    colores,
):
    if suma <= largo_fila:
        total_suma = sum(
            1 for i in range(largo_value_aleatorio + 2) if not tablero[y][x + i]
        )

        if total_suma == largo_value_aleatorio + 2:
            suma_caracter_value = 0
            for j in range(largo_value_aleatorio + 2):
                if j == 0 or j == largo_value_aleatorio + 1:
                    tablero[y][x + j] = bloque_relleno
                    suma_caracter_value += 1

                elif j == 1:
                    tablero[y][x + j] = value_aleatorio[0]
                    suma_caracter_value += 1
                else:
                    tablero[y][x + j] = caracter_vacio
                    suma_caracter_value += 1

                if largo_value_aleatorio + 2 == suma_caracter_value:
                    color_aleatorio = random.randint(0, len(colores) - 1)
                    color = colores[color_aleatorio]
                    numero_palabra += 1
                    datos_palabra = {
                        "numero_palabra": numero_palabra,
                        "fila": y,
                        "columna": x + 1,
                        "acertijo": key_aleatorio,
                        "respuesta": value_aleatorio,
                        "orientacion": "horizontal derecho",
                        "color": color,
                    }
                    return datos_palabra
        return
    return


def horizontal_izquierdo(
    y: int,
    x: int,
    resta: int,
    largo_value_aleatorio: int,
    tablero: list,
    bloque_relleno: str,
    value_aleatorio: str,
    key_aleatorio: str,
    caracter_vacio: str,
    numero_palabra: int,
    colores,
):
    if resta >= 0:
        total_suma = sum(
            1 for i in range(largo_value_aleatorio + 2) if not tablero[y][x - i]
        )

        if total_suma == largo_value_aleatorio + 2:
            suma_caracter_value = 0
            for h in range(largo_value_aleatorio + 2):
                if h == 0 or h == largo_value_aleatorio + 1:
                    tablero[y][x - h] = bloque_relleno
                    suma_caracter_value += 1

                elif h == 1:
                    tablero[y][x - h] = value_aleatorio[0]
                    suma_caracter_value += 1
                else:
                    tablero[y][x - h] = caracter_vacio
                    suma_caracter_value += 1

                if largo_value_aleatorio + 2 == suma_caracter_value:
                    color_aleatorio = random.randint(0, len(colores) - 1)
                    color = colores[color_aleatorio]
                    numero_palabra += 1
                    datos_palabra = {
                        "numero_palabra": numero_palabra,
                        "fila": y,
                        "columna": x - 1,
                        "acertijo": key_aleatorio,
                        "respuesta": value_aleatorio,
                        "orientacion": "horizontal izquierdo",
                        "color": color,
                    }
                    return datos_palabra

        return
    return


def vertical_abajo(
    y: int,
    x: int,
    suma: int,
    largo_columna: int,
    tablero: list,
    bloque_relleno: str,
    largo_value_aleatorio: int,
    value_aleatorio: int,
    caracter_vacio: str,
    key_aleatorio: int,
    numero_palabra: int,
    colores,
):
    if suma <= largo_columna:
        total_suma = sum(
            1 for i in range(largo_value_aleatorio + 2) if not tablero[y + i][x]
        )

        if total_suma == largo_value_aleatorio + 2:
            suma_caracter_value = 0
            for j in range(largo_value_aleatorio + 2):
                if j == 0 or j == largo_value_aleatorio + 1:
                    tablero[y + j][x] = bloque_relleno
                    suma_caracter_value += 1

                elif j == 1:
                    tablero[y + j][x] = value_aleatorio[0]
                    suma_caracter_value += 1

                else:
                    tablero[y + j][x] = caracter_vacio
                    suma_caracter_value += 1
                if largo_value_aleatorio + 2 == suma_caracter_value:
                    color_aleatorio = random.randint(0, len(colores) - 1)
                    color = colores[color_aleatorio]
                    numero_palabra += 1
                    datos_palabra = {
                        "numero_palabra": numero_palabra,
                        "fila": y + 1,
                        "columna": x,
                        "acertijo": key_aleatorio,
                        "respuesta": value_aleatorio,
                        "orientacion": "vertical abajo",
                        "color": color,
                    }
                    return datos_palabra
        return
    return


def vertical_arriba(
    y: int,
    x: int,
    resta: int,
    tablero: list,
    bloque_relleno: str,
    largo_value_aleatorio: int,
    value_aleatorio: int,
    caracter_vacio: str,
    key_aleatorio: str,
    numero_palabra: int,
    colores,
):
    if resta >= 0:
        total_suma = sum(
            1 for i in range(largo_value_aleatorio + 2) if not tablero[y - i][x]
        )

        if total_suma == largo_value_aleatorio + 2:
            suma_caracter_value = 0
            for i in range(largo_value_aleatorio + 2):
                if i == 0 or i == largo_value_aleatorio + 1:
                    tablero[y - i][x] = bloque_relleno
                    suma_caracter_value += 1

                elif i == 1:
                    tablero[y - i][x] = value_aleatorio[0]
                    suma_caracter_value += 1

                else:
                    tablero[y - i][x] = caracter_vacio
                    suma_caracter_value += 1
                if largo_value_aleatorio + 2 == suma_caracter_value:
                    color_aleatorio = random.randint(0, len(colores) - 1)
                    color = colores[color_aleatorio]
                    numero_palabra += 1
                    datos_palabra = {
                        "numero_palabra": numero_palabra,
                        "fila": y - 1,
                        "columna": x,
                        "acertijo": key_aleatorio,
                        "respuesta": value_aleatorio,
                        "orientacion": "vertical arriba",
                        "color": color,
                    }
                    return datos_palabra
        return
    return
