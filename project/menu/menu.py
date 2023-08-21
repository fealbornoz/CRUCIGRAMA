from project.tablero import tablero_matriz, rellenar_palabra_completa
import os
from colored import fore_rgb, style


def opt_invalida(opt: str, arreglo_indice: list) -> bool:
    return opt not in arreglo_indice


def opciones_listado(arreglo_completo: list) -> str:
    arreglo_indice = []
    for i in range(len(arreglo_completo)):
        arreglo_indice.append(str(arreglo_completo[i]["numero_palabra"]))

    opt = input("Ingrese algún número de definición: ")

    while opt_invalida(opt, arreglo_indice):
        opt = input(
            f"La opción ingresada [{opt}] es inválida, ingrese una que se encuentre: "
        )

    return opt


def imprimir_listado_indice(arreglo_completo: list) -> None:
    print(
        "\nRerefencia: [número de definicion]-[letra referenciada en el tablero]-[definicion]\n"
    )
    for i in arreglo_completo:
        rgb_0 = i["color"][0]
        rgb_1 = i["color"][1]
        rgb_2 = i["color"][2]
        print(
            f"[{i['numero_palabra']}]-{fore_rgb(rgb_0,rgb_1,rgb_2)}[{i['respuesta'][0]}]{style('reset')}-[{i['acertijo']}]"
        )


def listado_indice(
    arreglo_completo: list,
    tablero: list,
    palabras_completadas: int = 0,
    opcion: str = "",
    color: str = None,
    value_palabra: str = None,
) -> None:
    os.system("cls")
    tablero_matriz.imprimir(tablero, arreglo_completo)
    if opcion:
        rgb_0 = color[0]
        rgb_1 = color[1]
        rgb_2 = color[2]
        if opcion == "palabra correcta":
            print(
                f"\nRespuesta Correcta: {fore_rgb(rgb_0,rgb_1,rgb_2)}{value_palabra}{style('reset')}"
            )
        else:
            print(f"\nRespuesta Incorrecta\nComodín: {opcion}")
    if palabras_completadas == 12:
        print("¡Felicitaciones, ganaste!")
        return
    imprimir_listado_indice(arreglo_completo)
    opt = int(opciones_listado(arreglo_completo))

    for i in arreglo_completo:
        if i["numero_palabra"] == opt:
            y = i["fila"]
            x = i["columna"]
            value_palabra = i["respuesta"]
            tipo_de_palabra = i["orientacion"]
            color = i["color"]
            if tipo_de_palabra == "horizontal derecho":
                data = rellenar_palabra_completa.horizontal_derecho(
                    y,
                    x,
                    value_palabra,
                    tablero,
                    arreglo_completo,
                    palabras_completadas,
                    tipo_de_palabra,
                    color,
                )

                opcion = data["resultado"]
                if opcion == "palabra correcta":
                    arreglo_completo = data["arreglo_completo"]
                    palabras_completadas = data["palabras_completadas"]
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "reemplazar_palabra_aleatoria":
                    arreglo_completo = data["arreglo_completo"]
                    rgb_0 = data["color"][0]
                    rgb_1 = data["color"][1]
                    rgb_2 = data["color"][2]
                    opcion = f"{opcion}\nPalabra reemplazada: '{fore_rgb(rgb_0,rgb_1,rgb_2)}[{data['value_reemplazado'][0]}]{style('reset')}' por {fore_rgb(rgb_0,rgb_1,rgb_2)}[{data['value_nuevo'][0]}]{style('reset')}'"
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )
                elif opcion == "revelacion_palabra_comodin":
                    arreglo_completo = data["arreglo_completo"]
                    palabras_completadas = data["palabras_completadas"]
                    rgb_0 = data["color"][0]
                    rgb_1 = data["color"][1]
                    rgb_2 = data["color"][2]
                    opcion = f"{opcion}\nPalabra Revelada: '{fore_rgb(rgb_0,rgb_1,rgb_2)}{data['palabra_revelada']}{style('reset')}'"
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "revelacion_letras_vocales":
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "Fin Del Juego":
                    os.system("cls")
                    print(opcion)
                    return

                else:
                    return

            if tipo_de_palabra == "horizontal izquierdo":
                data = rellenar_palabra_completa.horizontal_izquierdo(
                    y,
                    x,
                    value_palabra,
                    tablero,
                    arreglo_completo,
                    palabras_completadas,
                    tipo_de_palabra,
                    color,
                )

                opcion = data["resultado"]
                if opcion == "palabra correcta":
                    arreglo_completo = data["arreglo_completo"]
                    palabras_completadas = data["palabras_completadas"]
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "reemplazar_palabra_aleatoria":
                    arreglo_completo = data["arreglo_completo"]
                    rgb_0 = data["color"][0]
                    rgb_1 = data["color"][1]
                    rgb_2 = data["color"][2]
                    opcion = f"{opcion}\nPalabra reemplazada: '{fore_rgb(rgb_0,rgb_1,rgb_2)}[{data['value_reemplazado'][0]}]{style('reset')}' por {fore_rgb(rgb_0,rgb_1,rgb_2)}[{data['value_nuevo'][0]}]{style('reset')}'"
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )
                elif opcion == "revelacion_palabra_comodin":
                    arreglo_completo = data["arreglo_completo"]
                    palabras_completadas = data["palabras_completadas"]
                    rgb_0 = data["color"][0]
                    rgb_1 = data["color"][1]
                    rgb_2 = data["color"][2]
                    opcion = f"{opcion}\nPalabra Revelada: '{fore_rgb(rgb_0,rgb_1,rgb_2)}{data['palabra_revelada']}{style('reset')}'"
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "revelacion_letras_vocales":
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "Fin Del Juego":
                    os.system("cls")
                    print(opcion)
                    return

                else:
                    return

            if tipo_de_palabra == "vertical abajo":
                data = rellenar_palabra_completa.vertical_abajo(
                    y,
                    x,
                    value_palabra,
                    tablero,
                    arreglo_completo,
                    palabras_completadas,
                    tipo_de_palabra,
                    color,
                )

                opcion = data["resultado"]
                if opcion == "palabra correcta":
                    arreglo_completo = data["arreglo_completo"]
                    palabras_completadas = data["palabras_completadas"]
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "reemplazar_palabra_aleatoria":
                    arreglo_completo = data["arreglo_completo"]
                    rgb_0 = data["color"][0]
                    rgb_1 = data["color"][1]
                    rgb_2 = data["color"][2]
                    opcion = f"{opcion}\nPalabra reemplazada: '{fore_rgb(rgb_0,rgb_1,rgb_2)}[{data['value_reemplazado'][0]}]{style('reset')}' por {fore_rgb(rgb_0,rgb_1,rgb_2)}[{data['value_nuevo'][0]}]{style('reset')}'"
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )
                elif opcion == "revelacion_palabra_comodin":
                    arreglo_completo = data["arreglo_completo"]
                    palabras_completadas = data["palabras_completadas"]
                    rgb_0 = data["color"][0]
                    rgb_1 = data["color"][1]
                    rgb_2 = data["color"][2]
                    opcion = f"{opcion}\nPalabra Revelada: '{fore_rgb(rgb_0,rgb_1,rgb_2)}{data['palabra_revelada']}{style('reset')}'"
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "revelacion_letras_vocales":
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "Fin Del Juego":
                    os.system("cls")
                    print(opcion)
                    return

                else:
                    return

            if tipo_de_palabra == "vertical arriba":
                data = rellenar_palabra_completa.vertical_arriba(
                    y,
                    x,
                    value_palabra,
                    tablero,
                    arreglo_completo,
                    palabras_completadas,
                    tipo_de_palabra,
                    color,
                )

                opcion = data["resultado"]
                if opcion == "palabra correcta":
                    arreglo_completo = data["arreglo_completo"]
                    palabras_completadas = data["palabras_completadas"]
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "reemplazar_palabra_aleatoria":
                    arreglo_completo = data["arreglo_completo"]
                    rgb_0 = data["color"][0]
                    rgb_1 = data["color"][1]
                    rgb_2 = data["color"][2]
                    opcion = f"{opcion}\nPalabra reemplazada: '{fore_rgb(rgb_0,rgb_1,rgb_2)}[{data['value_reemplazado'][0]}]{style('reset')}' por {fore_rgb(rgb_0,rgb_1,rgb_2)}[{data['value_nuevo'][0]}]{style('reset')}'"
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )
                elif opcion == "revelacion_palabra_comodin":
                    arreglo_completo = data["arreglo_completo"]
                    palabras_completadas = data["palabras_completadas"]
                    rgb_0 = data["color"][0]
                    rgb_1 = data["color"][1]
                    rgb_2 = data["color"][2]
                    opcion = f"{opcion}\nPalabra Revelada: '{fore_rgb(rgb_0,rgb_1,rgb_2)}{data['palabra_revelada']}{style('reset')}'"
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "revelacion_letras_vocales":
                    return listado_indice(
                        arreglo_completo,
                        tablero,
                        palabras_completadas,
                        opcion,
                        color,
                        value_palabra,
                    )

                elif opcion == "Fin Del Juego":
                    os.system("cls")
                    print(opcion)
                    return

                else:
                    return
