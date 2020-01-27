# Intentar resolver usando las distintas búsquedas y en su caso, las distintas
# heurísticas, el problema del 8 puzzle para los siguientes estados iniciales:

# E1 E2 E3 E4
#
# +---+---+---+ +---+---+---+ +---+---+---+ +---+---+---+
# | 2 | 8 | 3 | | 4 | 8 | 1 | | 2 | 1 | 6 | | 5 | 2 | 3 |
# +---+---+---+ +---+---+---+ +---+---+---+ +---+---+---+
# | 1 | 6 | 4 | | 3 | H | 2 | | 4 | H | 8 | | H | 4 | 8 |
# +---+---+---+ +---+---+---+ +---+---+---+ +---+---+---+
# | 7 | H | 5 | | 7 | 6 | 5 | | 7 | 5 | 3 | | 7 | 6 | 1 |
# +---+---+---+ +---+---+---+ +---+---+---+ +---+---+---+

# Se pide, en cada caso, hacerlo con la función resuelve_ocho_puzzle, para obtener, además de la solución, la longitud (el coste) de la solución
# obtenida y el número de nodos analizados. Anotar los resultados en la siguiente tabla (L, longitud de la solución, NA, nodos analizados), y
# justificarlos con las distintas propiedades teóricas estudiadas.
# ------------------------------------------------------------------------ -----------------

from class_problema_estadisticas import *
from algoritmos_de_busqueda import *
from ejer03_heuristica import *

E1 = (2, 8, 3, 1, 6, 4, 7, 0, 5)
E2 = (4, 8, 1, 3, 0, 2, 7, 6, 5)
E3 = (2, 1, 6, 4, 0, 8, 7, 5, 3)
E4 = (5, 2, 3, 0, 4, 8, 7, 6, 1)

E1_result = resuelve_ocho_puzzle(E1, algoritmo=busqueda_a_estrella, h=h2_ocho_puzzle)
E2_result = resuelve_ocho_puzzle(E2, algoritmo=busqueda_en_profundidad)
E3_result = resuelve_ocho_puzzle(E3, algoritmo=busqueda_primero_el_mejor)
E4_result = resuelve_ocho_puzzle(E4, algoritmo=busqueda_a_estrella, h=h2_ocho_puzzle)

print(E1_result)
