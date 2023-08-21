from project.renglones import renglones
from project.listado_de_palabras import listado
from project.tablero import tablero_matriz
import random
from colored import fore_rgb, style


def opciones(
    y: int,
    x: int,
    value_palabra: str,
    color: list,
    tablero: list,
    tipo_de_palabra: str,
    arreglo_completo: list,
    palabras_completadas: int,
):
    dado = random.randint(1, 6)

    if dado == 1 or dado == 2:
        data = reemplazar_palabra_aleatoria(
            y, x, value_palabra, color, tablero, tipo_de_palabra, arreglo_completo
        )
        return {
            "resultado": "reemplazar_palabra_aleatoria",
            "arreglo_completo": data["arreglo_completo"],
            "value_reemplazado": data["value_reemplazado"],
            "value_nuevo": data["value_nuevo"],
            "color": data["color"],
        }

    if dado == 3 or dado == 4:
        revelacion_letras_vocales(y, x, tablero, arreglo_completo)
        return {"resultado": "revelacion_letras_vocales"}

    if dado == 5:
        data = revelacion_palabra_comodin(
            arreglo_completo, tablero, palabras_completadas
        )
        return {
            "resultado": "revelacion_palabra_comodin",
            "arreglo_completo": data["arreglo_completo"],
            "palabras_completadas": data["palabras_completadas"],
            "palabra_revelada": data["palabra_revelada"],
            "color":data["color"]
        }

    if dado == 6:
        return {"resultado": "Fin Del Juego"}


def reemplazar_palabra_aleatoria(
    y: int,
    x: int,
    value_palabra: str,
    color: list,
    tablero: list,
    tipo_de_palabra: str,
    arreglo_completo: list,
    relleno: int = 0,
) -> None:
    bloque_relleno = "\u2587"
    if tipo_de_palabra == "horizontal derecho":
        if relleno == 0:
            for i in range(len(value_palabra)):
                tablero[y][x + i] = bloque_relleno
            relleno += 1

        x = random.randint(0, 19)
        y = random.randint(0, 19)
        caracter_vacio = " "
        posicion_aleatoria = random.randint(0, 52)
        key_listado = listado.definiciones.keys()
        key_aleatorio = list(key_listado)[posicion_aleatoria]
        value_listado = listado.definiciones.values()
        value_aleatorio = list(value_listado)[posicion_aleatoria]
        largo_fila = len(tablero[0])
        largo_value_aleatorio = len(value_aleatorio)
        suma = x + (largo_value_aleatorio + 2)
        resta = x + (largo_value_aleatorio + 2)
        if suma <= largo_fila and renglones.value_repetido(
            arreglo_completo, value_aleatorio
        ):
            total_suma = 0
            for i in range(largo_value_aleatorio + 2):
                if tablero[y][x + i] == bloque_relleno:
                    total_suma += 1

            if total_suma == largo_value_aleatorio + 2:
                suma_caracter_value = 0
                for j in range(largo_value_aleatorio + 2):
                    if j == 0:
                        tablero[y][x + j] = bloque_relleno
                        suma_caracter_value += 1

                    elif j == 1:
                        tablero[y][x + j] = value_aleatorio[0]
                        suma_caracter_value += 1

                    elif j == largo_value_aleatorio + 1:
                        tablero[y][x + j] = bloque_relleno
                        suma_caracter_value += 1
                    else:
                        tablero[y][x + j] = caracter_vacio
                        suma_caracter_value += 1

                    if largo_value_aleatorio + 2 == suma_caracter_value:
                        for k in range(len(arreglo_completo)):
                            if arreglo_completo[k]["respuesta"] == value_palabra:
                                arreglo_completo[k]["fila"] = y
                                arreglo_completo[k]["columna"] = x + 1
                                arreglo_completo[k]["acertijo"] = key_aleatorio
                                arreglo_completo[k]["respuesta"] = value_aleatorio
                        return {
                            "arreglo_completo": arreglo_completo,
                            "value_reemplazado": value_palabra,
                            "value_nuevo": value_aleatorio,
                            "color": color,
                        }

            else:
                return reemplazar_palabra_aleatoria(
                    y,
                    x,
                    value_palabra,
                    color,
                    tablero,
                    tipo_de_palabra,
                    arreglo_completo,
                    relleno,
                )

        else:
            return reemplazar_palabra_aleatoria(
                y,
                x,
                value_palabra,
                color,
                tablero,
                tipo_de_palabra,
                arreglo_completo,
                relleno,
            )

    if tipo_de_palabra == "horizontal izquierdo":
        if relleno == 0:
            for i in range(len(value_palabra)):
                tablero[y][x - i] = bloque_relleno
            relleno += 1
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        caracter_vacio = " "
        posicion_aleatoria = random.randint(0, 52)
        key_listado = listado.definiciones.keys()
        key_aleatorio = list(key_listado)[posicion_aleatoria]
        value_listado = listado.definiciones.values()
        value_aleatorio = list(value_listado)[posicion_aleatoria]
        largo_fila = len(tablero[0])
        largo_value_aleatorio = len(value_aleatorio)
        suma = x + (largo_value_aleatorio + 2)
        resta = x - (largo_value_aleatorio + 2)
        if resta >= 0 and renglones.value_repetido(arreglo_completo, value_aleatorio):
            total_suma = 0
            for f in range(largo_value_aleatorio + 2):
                if tablero[y][x - f] == bloque_relleno:
                    total_suma += 1

            if total_suma == largo_value_aleatorio + 2:
                suma_caracter_value = 0
                for h in range(largo_value_aleatorio + 2):
                    if h == 0:
                        tablero[y][x - h] = bloque_relleno
                        suma_caracter_value += 1

                    elif h == 1:
                        tablero[y][x - h] = value_aleatorio[0]
                        suma_caracter_value += 1

                    elif h == largo_value_aleatorio + 1:
                        tablero[y][x - h] = bloque_relleno
                        suma_caracter_value += 1

                    else:
                        tablero[y][x - h] = caracter_vacio
                        suma_caracter_value += 1

                    if largo_value_aleatorio + 2 == suma_caracter_value:
                        for k in range(len(arreglo_completo)):
                            if arreglo_completo[k]["respuesta"] == value_palabra:
                                arreglo_completo[k]["fila"] = y
                                arreglo_completo[k]["columna"] = x - 1
                                arreglo_completo[k]["acertijo"] = key_aleatorio
                                arreglo_completo[k]["respuesta"] = value_aleatorio
                        return {
                            "arreglo_completo": arreglo_completo,
                            "value_reemplazado": value_palabra,
                            "value_nuevo": value_aleatorio,
                            "color": color,
                        }

            else:
                return reemplazar_palabra_aleatoria(
                    y,
                    x,
                    value_palabra,
                    color,
                    tablero,
                    tipo_de_palabra,
                    arreglo_completo,
                    relleno,
                )

        else:
            return reemplazar_palabra_aleatoria(
                y, x, value_palabra,color, tablero, tipo_de_palabra, arreglo_completo, relleno
            )

    if tipo_de_palabra == "vertical abajo":
        if relleno == 0:
            for i in range(len(value_palabra)):
                tablero[y + i][x] = bloque_relleno
            relleno += 1

        x = random.randint(0, 19)
        y = random.randint(0, 19)
        caracter_vacio = " "
        posicion_aleatoria = random.randint(0, 52)
        key_listado = listado.definiciones.keys()
        key_aleatorio = list(key_listado)[posicion_aleatoria]
        value_listado = listado.definiciones.values()
        value_aleatorio = list(value_listado)[posicion_aleatoria]
        largo_columna = len(tablero) - 1
        largo_value_aleatorio = len(value_aleatorio)
        suma = y + (largo_value_aleatorio + 2)
        resta = y - (largo_value_aleatorio + 2)
        if suma <= largo_columna and renglones.value_repetido(
            arreglo_completo, value_aleatorio
        ):
            total_suma1 = 0
            for i in range(largo_value_aleatorio + 2):
                if tablero[y + i][x] == bloque_relleno:
                    total_suma1 += 1

            if total_suma1 == largo_value_aleatorio + 2:
                suma_caracter_value = 0
                for j in range(largo_value_aleatorio + 2):
                    if j == 0:
                        tablero[y + j][x] = bloque_relleno
                        suma_caracter_value += 1

                    elif j == 1:
                        tablero[y + j][x] = value_aleatorio[0]
                        suma_caracter_value += 1

                    elif j == largo_value_aleatorio + 1:
                        tablero[y + j][x] = bloque_relleno
                        suma_caracter_value += 1

                    else:
                        tablero[y + j][x] = caracter_vacio
                        suma_caracter_value += 1
                    if largo_value_aleatorio + 2 == suma_caracter_value:
                        for k in range(len(arreglo_completo)):
                            if arreglo_completo[k]["respuesta"] == value_palabra:
                                arreglo_completo[k]["fila"] = y + 1
                                arreglo_completo[k]["columna"] = x
                                arreglo_completo[k]["acertijo"] = key_aleatorio
                                arreglo_completo[k]["respuesta"] = value_aleatorio
                        return {
                            "arreglo_completo": arreglo_completo,
                            "value_reemplazado": value_palabra,
                            "value_nuevo": value_aleatorio,
                            "color": color,
                        }

            else:
                return reemplazar_palabra_aleatoria(
                    y,
                    x,
                    value_palabra,
                    color,
                    tablero,
                    tipo_de_palabra,
                    arreglo_completo,
                    relleno,
                )

        else:
            return reemplazar_palabra_aleatoria(
                y, x, value_palabra,color, tablero, tipo_de_palabra, arreglo_completo, relleno
            )

    if tipo_de_palabra == "vertical arriba":
        if relleno == 0:
            for i in range(len(value_palabra)):
                tablero[y - i][x] = bloque_relleno
            relleno += 1
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        caracter_vacio = " "
        posicion_aleatoria = random.randint(0, 52)
        key_listado = listado.definiciones.keys()
        key_aleatorio = list(key_listado)[posicion_aleatoria]
        value_listado = listado.definiciones.values()
        value_aleatorio = list(value_listado)[posicion_aleatoria]
        largo_columna = len(tablero) - 1
        largo_value_aleatorio = len(value_aleatorio)
        suma = y + (largo_value_aleatorio + 2)
        resta = y - (largo_value_aleatorio + 2)
        if resta >= 0 and renglones.value_repetido(arreglo_completo, value_aleatorio):
            total_suma = 0
            for i in range(largo_value_aleatorio + 2):
                if tablero[y - i][x] == bloque_relleno:
                    total_suma += 1

            if total_suma == largo_value_aleatorio + 2:
                suma_caracter_value = 0
                for i in range(largo_value_aleatorio + 2):
                    if i == 0:
                        tablero[y - i][x] = bloque_relleno
                        suma_caracter_value += 1

                    elif i == 1:
                        tablero[y - i][x] = value_aleatorio[0]
                        suma_caracter_value += 1

                    elif i == largo_value_aleatorio + 1:
                        tablero[y - i][x] = bloque_relleno
                        suma_caracter_value += 1

                    else:
                        tablero[y - i][x] = caracter_vacio
                        suma_caracter_value += 1
                    if largo_value_aleatorio + 2 == suma_caracter_value:
                        for k in range(len(arreglo_completo)):
                            if arreglo_completo[k]["respuesta"] == value_palabra:
                                arreglo_completo[k]["fila"] = y - 1
                                arreglo_completo[k]["columna"] = x
                                arreglo_completo[k]["acertijo"] = key_aleatorio
                                arreglo_completo[k]["respuesta"] = value_aleatorio
                        return {
                            "arreglo_completo": arreglo_completo,
                            "value_reemplazado": value_palabra,
                            "value_nuevo": value_aleatorio,
                            "color": color,
                        }

            else:
                return reemplazar_palabra_aleatoria(
                    y,
                    x,
                    value_palabra,
                    color,
                    tablero,
                    tipo_de_palabra,
                    arreglo_completo,
                    relleno,
                )

        else:
            return reemplazar_palabra_aleatoria(
                y, x, value_palabra,color, tablero, tipo_de_palabra, arreglo_completo, relleno
            )


# numero_palabra = 0
# reemplazar_palabra = True
# datos_palabra_tablero = rellenar_espacio_palabra.horizontal_derecho(
#     y,
#     x,
#     suma,
#     largo_fila,
#     largo_value_aleatorio,
#     tablero,
#     bloque_relleno,
#     value_aleatorio,
#     key_aleatorio,
#     caracter_vacio,
#     numero_palabra,
#     reemplazar_palabra,
# )
# datos_palabra = datos_palabra_tablero[0]
# tablero = datos_palabra_tablero[1]
# arreglo_completo_seteado = renglones.sacar_value_poner_nuevo(
#     arreglo_completo, value_palabra, datos_palabra
# )
# return {"tablero": tablero, "arreglo_completo": arreglo_completo_seteado}


def rellenar_vocales_palabra(
    y: int, x: int, value_palabra: str, tablero: list, tipo_de_palabra: str, color
) -> None:
    vocales = ["a", "e", "i", "o", "u"]
    rgb_0 = color[0]
    rgb_1 = color[1]
    rgb_2 = color[2]
    if tipo_de_palabra == "horizontal derecho":
        for i in range(len(value_palabra)):
            for j in range(len(vocales)):
                letra_value_palabra = value_palabra[i]
                if letra_value_palabra == vocales[j]:
                    tablero[y][x + i] = (
                        fore_rgb(rgb_0, rgb_1, rgb_2) + vocales[j] + style("reset")
                    )

    if tipo_de_palabra == "horizontal izquierdo":
        for i in range(len(value_palabra)):
            for j in range(len(vocales)):
                letra_value_palabra = value_palabra[i]
                if letra_value_palabra == vocales[j]:
                    tablero[y][x - i] = (
                        fore_rgb(rgb_0, rgb_1, rgb_2) + vocales[j] + style("reset")
                    )

    if tipo_de_palabra == "vertical abajo":
        for i in range(len(value_palabra)):
            for j in range(len(vocales)):
                letra_value_palabra = value_palabra[i]
                if letra_value_palabra == vocales[j]:
                    tablero[y + i][x] = (
                        fore_rgb(rgb_0, rgb_1, rgb_2) + vocales[j] + style("reset")
                    )

    if tipo_de_palabra == "vertical arriba":
        for i in range(len(value_palabra)):
            for j in range(len(vocales)):
                letra_value_palabra = value_palabra[i]
                if letra_value_palabra == vocales[j]:
                    tablero[y - i][x] = (
                        fore_rgb(rgb_0, rgb_1, rgb_2) + vocales[j] + style("reset")
                    )
    return


def revelacion_letras_vocales(
    y: int, x: int, tablero: list, arreglo_completo: list
) -> None:
    for i in range(len(arreglo_completo)):
        y = arreglo_completo[i]["fila"]
        x = arreglo_completo[i]["columna"]
        value_palabra = arreglo_completo[i]["respuesta"]
        tipo_de_palabra = arreglo_completo[i]["orientacion"]
        color = arreglo_completo[i]["color"]
        if tipo_de_palabra == "horizontal derecho":
            rellenar_vocales_palabra(
                y, x, value_palabra, tablero, tipo_de_palabra, color
            )
        if tipo_de_palabra == "horizontal izquierdo":
            rellenar_vocales_palabra(
                y, x, value_palabra, tablero, tipo_de_palabra, color
            )
        if tipo_de_palabra == "vertical abajo":
            rellenar_vocales_palabra(
                y, x, value_palabra, tablero, tipo_de_palabra, color
            )
        if tipo_de_palabra == "vertical arriba":
            rellenar_vocales_palabra(
                y, x, value_palabra, tablero, tipo_de_palabra, color
            )

    return


def revelacion_palabra_comodin(
    arreglo_completo: list,
    tablero: list,
    palabras_completadas,
) -> None:
    aleatorio = random.randint(0, len(arreglo_completo) - 1)
    y = arreglo_completo[aleatorio]["fila"]
    x = arreglo_completo[aleatorio]["columna"]
    tipo_de_palabra = arreglo_completo[aleatorio]["orientacion"]
    palabra_aleatoria_value = arreglo_completo[aleatorio]["respuesta"]
    color = arreglo_completo[aleatorio]["color"]
    rgb_0 = color[0]
    rgb_1 = color[1]
    rgb_2 = color[2]
    if tipo_de_palabra == "horizontal derecho":
        for i in range(len(palabra_aleatoria_value)):
            tablero[y][x + i] = (
                fore_rgb(rgb_0, rgb_1, rgb_2)
                + palabra_aleatoria_value[i]
                + style("reset")
            )
        palabras_completadas += 1
        arreglo_completo = list(
            filter(
                lambda i: i["respuesta"] != palabra_aleatoria_value, arreglo_completo
            )
        )
        return {
            "arreglo_completo": arreglo_completo,
            "palabras_completadas": palabras_completadas,
            "palabra_revelada": palabra_aleatoria_value,
            "color": color,
        }

    if tipo_de_palabra == "horizontal izquierdo":
        for i in range(len(palabra_aleatoria_value)):
            tablero[y][x - i] = (
                fore_rgb(rgb_0, rgb_1, rgb_2)
                + palabra_aleatoria_value[i]
                + style("reset")
            )
        palabras_completadas += 1
        arreglo_completo = list(
            filter(
                lambda i: i["respuesta"] != palabra_aleatoria_value, arreglo_completo
            )
        )
        return {
            "arreglo_completo": arreglo_completo,
            "palabras_completadas": palabras_completadas,
            "palabra_revelada": palabra_aleatoria_value,
            "color": color,
        }

    if tipo_de_palabra == "vertical abajo":
        for i in range(len(palabra_aleatoria_value)):
            tablero[y + i][x] = (
                fore_rgb(rgb_0, rgb_1, rgb_2)
                + palabra_aleatoria_value[i]
                + style("reset")
            )
        palabras_completadas += 1
        arreglo_completo = list(
            filter(
                lambda i: i["respuesta"] != palabra_aleatoria_value, arreglo_completo
            )
        )
        return {
            "arreglo_completo": arreglo_completo,
            "palabras_completadas": palabras_completadas,
            "palabra_revelada": palabra_aleatoria_value,
            "color": color,
        }

    if tipo_de_palabra == "vertical arriba":
        for i in range(len(palabra_aleatoria_value)):
            tablero[y - i][x] = (
                fore_rgb(rgb_0, rgb_1, rgb_2)
                + palabra_aleatoria_value[i]
                + style("reset")
            )
        palabras_completadas += 1
        arreglo_completo = list(
            filter(
                lambda i: i["respuesta"] != palabra_aleatoria_value, arreglo_completo
            )
        )
        return {
            "arreglo_completo": arreglo_completo,
            "palabras_completadas": palabras_completadas,
            "palabra_revelada": palabra_aleatoria_value,
            "color": color,
        }
