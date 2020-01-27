from class_problema import *


class Ocho_Puzzle(Problema):

    def __init__(self, tablero_inicial):
        self.estado_inicial = tablero_inicial
        self.estado_final = (1, 2, 3, 8, 0, 4, 7, 6, 5)

    def acciones(self, estado):
        pos_hueco = estado.index(0)
        accs = list()
        if pos_hueco not in (0, 1, 2):
            accs.append("Mover hueco arriba")
        if pos_hueco not in (0, 3, 6):
            accs.append("Mover hueco izquierda")
        if pos_hueco not in (6, 7, 8):
            accs.append("Mover hueco abajo")
        if pos_hueco not in (2, 5, 8):
            accs.append("Mover hueco derecha")
        return accs

    def aplica(self, estado, accion):
         pos_hueco = estado.index(0)
         l = list(estado)
         if accion == "Mover hueco arriba":
             l[pos_hueco] = l[pos_hueco-3]
             l[pos_hueco-3] = 0
         if accion == "Mover hueco abajo":
             l[pos_hueco] = l[pos_hueco+3]
             l[pos_hueco+3] = 0
         if accion == "Mover hueco derecha":
             l[pos_hueco] = l[pos_hueco+1]
             l[pos_hueco+1] = 0
         if accion == "Mover hueco izquierda":
             l[pos_hueco] = l[pos_hueco-1]
             l[pos_hueco-1] = 0
         return tuple(l)


# EXAMPLE:


#p8p_1 = Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))
#print(p8p_1.estado_inicial)
#print(p8p_1.estado_final)
#print(p8p_1.acciones(p8p_1.estado_inicial))
#print(p8p_1.aplica(p8p_1.estado_inicial,"Mover hueco arriba"))
#print(p8p_1.coste_de_aplicar_accion(p8p_1.estado_inicial,"Mover hueco arriba"))























