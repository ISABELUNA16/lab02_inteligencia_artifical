#  Definir las dos funciones heurísticas para el 8 puzzle:
# - h1_ocho_puzzle(estado): cuenta el número de casillas mal colocadas respecto
#   del estado final.
# - h2_ocho_puzzle_estado(estado): suma la distancia Manhattan desde cada casilla
#   a la posición en la que debería estar en el estado final.


def h1_ocho_puzzle(estado):
    estado_final = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    l = sum([1 for i in range(9) if estado[i] == estado_final[i]])
    return l


def posiciones(estado):
    ''' Función auxiliar que determina las coordenadas de la tupla estado en una mátrix '''
    l = list()
    for i in estado:
        indice = estado.index(i)
        if indice in (0, 1, 2):
            l.append((i, 0, estado.index(i) % 3))
        if indice in (3, 4, 5):
            l.append((i, 1, estado.index(i) % 3))
        if indice in (6, 7, 8):
            l.append((i, 2, estado.index(i) % 3))
    return l


def h2_ocho_puzzle(estado):
    estado_final = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    final_pos = posiciones(estado_final)
    estado_pos = posiciones(estado)
    t = 0
    for i in final_pos:
        for j in range(9):
            if estado_pos[j][0] == i[0] and i[0] != 0:
                t += abs(i[1]-estado_pos[j][1])
                t += abs(i[2]-estado_pos[j][2])
    return t

# EXAMPLE:


#print(h1_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5)))
#print(h2_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5)))
#print(h1_ocho_puzzle((5, 2, 3, 0, 4, 8, 7, 6, 1)))
#print(h2_ocho_puzzle((5, 2, 3, 0, 4, 8, 7, 6, 1)))



























