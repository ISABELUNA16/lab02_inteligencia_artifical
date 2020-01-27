
# Resolver usando búsqueda_coste:uniforme, búsqueda_primero_
# el_mejor y búsqueda_a_estrella (con las dos heurísticas),
# el problema del 8 puzzle
# para el siguiente estado inicial:
# +---+---+---+
# | 2 | 8 | 3 |
# +---+---+---+
# | 1 | 6 | 4 |
# +---+---+---+
# | 7 | H | 5 |
# +---+---+---+

from algoritmos_de_busqueda import *
from ejer01_class_ocho_puzzle import *


puzzle = Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))
print(busqueda_coste_uniforme(puzzle).solucion())
