from project.menu import menu
from project.renglones import renglones
from project.tablero import tablero_matriz
from project.listado_de_palabras import listado


def main() -> None:
    tablero = tablero_matriz.armado_tablero_vacio()
    colores = listado.colores
    arreglo_completo = renglones.horizontales_verticales(tablero,colores)
    tablero_matriz.rellenar_espacios_vacios(tablero)
    menu.listado_indice(arreglo_completo, tablero)
    return

main()