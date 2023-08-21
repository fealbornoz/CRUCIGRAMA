from colored import fore_rgb, style


def armado_tablero_vacio() -> list:
    tablero = []
    fila = []
    n = 20
    m = 20
    for i in range(m):
        fila.append("")

    for i in range(n):
        tablero.append([x for x in fila])

    return tablero


def rellenar_espacios_vacios(tablero: list) -> None:
    bloque_relleno = "\u2587"
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if not tablero[i][j]:
                tablero[i][j] = bloque_relleno
    return tablero


def imprimir(tablero: list, arreglo_completo) -> None:
    bloque_relleno = "\u2587"
    suma = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            for k in range(len(arreglo_completo)):
                if (
                    arreglo_completo[k]["fila"] == i
                    and arreglo_completo[k]["columna"] == j
                ):
                    suma += 1
                    rgb_0 = arreglo_completo[k]["color"][0]
                    rgb_1 = arreglo_completo[k]["color"][1]
                    rgb_2 = arreglo_completo[k]["color"][2]
                    print(
                        f"{fore_rgb(rgb_0,rgb_1,rgb_2)}{tablero[i][j]}{style('reset')}",
                        end=" ",
                    )

            if suma == 0:
                if tablero[i][j] == bloque_relleno:
                    print(f"{fore_rgb(170,170,170)}{tablero[i][j]}", end=" ")
                else:
                    print(tablero[i][j], end=" ")

            suma = 0

        print("")

    return
