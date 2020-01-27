from ejer01_class_ocho_puzzle import *


class Problema_con_Analizados(Problema):

    """Es un problema que se comporta exactamente igual que el que recibe al
       inicializarse, y además incorpora unos atributos nuevos para almacenar el
       número de nodos analizados durante la búsqueda. De esta manera, no
       tenemos que modificar el código del algoritmo de búsqueda."""

    def __init__(self, problema):
        self.estado_inicial = problema.estado_inicial
        self.problema = problema
        self.analizados  = 0

    def acciones(self, estado):
        return self.problema.acciones(estado)

    def aplica(self, estado, accion):
        return self.problema.aplica(estado, accion)

    def es_estado_final(self, estado):
        self.analizados += 1
        return self.problema.es_estado_final(estado)

    def coste_de_aplicar_accion(self, estado, accion):
        return self.problema.coste_de_aplicar_accion(estado, accion)


def resuelve_ocho_puzzle(estado_inicial, algoritmo, h=None):

    """Función para aplicar un algoritmo de búsqueda dado al problema del ocho
       puzzle, con un estado inicial dado y (cuando el algoritmo lo necesite)
       una heurística dada.
       Ejemplo de uso:
       resuelve_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5),búsqueda_a_estrella,h2_ocho_puzzle)
       Solución: ['Mover hueco arriba', 'Mover hueco arriba', 'Mover hueco izquierda',
                  'Mover hueco abajo', 'Mover hueco derecha']
       Algoritmo: búsqueda_a_estrella
       Heurística: h2_ocho_puzzle
       Longitud de la solución: 5. Nodos analizados: 7
       """

    p8p = Problema_con_Analizados(Ocho_Puzzle(estado_inicial))
    sol = (algoritmo(p8p,h).solucion() if h else algoritmo(p8p).solucion())
    print("Solución: {0}".format(sol))
    print("Algoritmo: {0}".format(algoritmo.__name__))
    if h:
        print("Heurística: {0}".format(h.__name__))
    else:
        pass
    print("Longitud de la solución: {0}. Nodos analizados: {1}".format(len(sol), p8p.analizados))
