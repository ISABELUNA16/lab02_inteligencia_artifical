from algoritmos_de_busqueda import *
from class_jarras import *
from ejer01_class_ocho_puzzle import *

# Usar búsqueda en anchura y en profundidad para encontrar soluciones tanto al
# problema de las jarras como al problema del ocho puzzle con distintos
# estados iniciales.

print(busqueda_en_anchura(Jarras()).solucion())
print(busqueda_en_profundidad(Jarras()).solucion())
print(busqueda_en_anchura(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))).solucion())
print(busqueda_en_profundidad(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))).solucion())
