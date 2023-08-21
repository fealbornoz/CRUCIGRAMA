# Presentación
<p>Este es un juego realizado en python, el mismo consiste en un crucigrama de 12 palabras de tamaño
variable y elegidas al azar de un listado de al menos 50 con sus respectivas definiciones (al final de
este enunciado se lista un ejemplo).</p>
<p></p>El crucigrama estará compuesto por:</p>
<p></p>● un tablero fijo de 20x20</p>
<p></p>● 6 palabras horizontales (tanto de izquierda a derecha como viceversa)</p>
<p></p>● 6 palabras verticales (tanto de arriba hacia abajo como viceversa)</p>
<p></p>● casilleros “libres” representados por el caracter ASCII 219</p>
<p>Cabe destacar que las palabras elegidas al azar por el programa se ajustan al tablero fijo.</p>


## Jugadas Especiales
<p>Por cada palabra errada se tirará un dado (al azar). Si sale:</p>
<p></p>● 1 ó 2: el usuario pierde una de las palabras que haya completado y se agrega una nueva del
listado (hay que volver a rearmar el dibujo del crucigrama).</p>
<p></p>● 3 ó 4: se descubren todas las vocales de las palabras faltantes.</p>
<p></p>● 5: el usuario puede elegir una palabra comodín (esa palabra se descubrirá por sí sola en el
crucigrama).</p>
<p></p>● 6: ¡dado de la muerte! se pierde el juego.</p>


# Running

Para correr el juego, se tiene que clonar este repositorio y estar para en el proyecto en la consola, en éste último colocar "python main.py".


