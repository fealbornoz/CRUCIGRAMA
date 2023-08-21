from project.dados import dados
from colored import fore_rgb, style


def horizontal_derecho(
    y: int,
    x: int,
    value_palabra: str,
    tablero: list,
    arreglo_completo: list,
    palabras_completadas: int,
    tipo_de_palabra: str,
    color,
):
    palabra_ingresada = input("Ingrese la palabra que cree saber que es: ")

    if palabra_ingresada != value_palabra:
        opciones = dados.opciones(
            y,
            x,
            value_palabra,
            color,
            tablero,
            tipo_de_palabra,
            arreglo_completo,
            palabras_completadas,
        )
        return opciones

    else:
        for i in range(len(value_palabra)):
            rgb_0 = color[0]
            rgb_1 = color[1]
            rgb_2 = color[2]
            tablero[y][x + i] = (
                fore_rgb(rgb_0, rgb_1, rgb_2) + value_palabra[i] + style("reset")
            )

        palabras_completadas += 1
        arreglo_completo = list(
            filter(lambda i: i["respuesta"] != value_palabra, arreglo_completo)
        )

        return {
            "resultado": "palabra correcta",
            "arreglo_completo": arreglo_completo,
            "palabras_completadas": palabras_completadas,
        }


def horizontal_izquierdo(
    y: int,
    x: int,
    value_palabra: str,
    tablero: list,
    arreglo_completo: list,
    palabras_completadas: int,
    tipo_de_palabra: str,
    color,
) -> None:
    palabra_ingresada = input("Ingrese la palabra que cree saber que es: ")

    if palabra_ingresada != value_palabra:
        opciones = dados.opciones(
            y,
            x,
            value_palabra,
            color,
            tablero,
            tipo_de_palabra,
            arreglo_completo,
            palabras_completadas,
        )
        return opciones
    else:
        for i in range(len(value_palabra)):
            rgb_0 = color[0]
            rgb_1 = color[1]
            rgb_2 = color[2]
            tablero[y][x - i] = (
                fore_rgb(rgb_0, rgb_1, rgb_2) + value_palabra[i] + style("reset")
            )

        palabras_completadas += 1
        arreglo_completo = list(
            filter(lambda i: i["respuesta"] != value_palabra, arreglo_completo)
        )
        return {
            "resultado": "palabra correcta",
            "arreglo_completo": arreglo_completo,
            "palabras_completadas": palabras_completadas,
        }


def vertical_abajo(
    y: int,
    x: int,
    value_palabra: str,
    tablero: list,
    arreglo_completo: list,
    palabras_completadas: int,
    tipo_de_palabra: str,
    color,
) -> None:
    palabra_ingresada = input("Ingrese la palabra que cree saber que es: ")

    if palabra_ingresada != value_palabra:
        opciones = dados.opciones(
            y,
            x,
            value_palabra,
            color,
            tablero,
            tipo_de_palabra,
            arreglo_completo,
            palabras_completadas,
        )
        return opciones
    else:
        for i in range(len(value_palabra)):
            rgb_0 = color[0]
            rgb_1 = color[1]
            rgb_2 = color[2]
            tablero[y + i][x] = (
                fore_rgb(rgb_0, rgb_1, rgb_2) + value_palabra[i] + style("reset")
            )

        palabras_completadas += 1
        arreglo_completo = list(
            filter(lambda i: i["respuesta"] != value_palabra, arreglo_completo)
        )
        return {
            "resultado": "palabra correcta",
            "arreglo_completo": arreglo_completo,
            "palabras_completadas": palabras_completadas,
        }


def vertical_arriba(
    y: int,
    x: int,
    value_palabra: str,
    tablero: list,
    arreglo_completo: list,
    palabras_completadas: int,
    tipo_de_palabra: str,
    color,
) -> None:
    palabra_ingresada = input("Ingrese la palabra que cree saber que es: ")

    if palabra_ingresada != value_palabra:
        opciones = dados.opciones(
            y,
            x,
            value_palabra,
            color,
            tablero,
            tipo_de_palabra,
            arreglo_completo,
            palabras_completadas,
        )
        return opciones
    else:
        for i in range(len(value_palabra)):
            rgb_0 = color[0]
            rgb_1 = color[1]
            rgb_2 = color[2]
            tablero[y - i][x] = (
                fore_rgb(rgb_0, rgb_1, rgb_2) + value_palabra[i] + style("reset")
            )

        palabras_completadas += 1
        arreglo_completo = list(
            filter(lambda i: i["respuesta"] != value_palabra, arreglo_completo)
        )
        return {
            "resultado": "palabra correcta",
            "arreglo_completo": arreglo_completo,
            "palabras_completadas": palabras_completadas,
        }
