from ejer03_heuristica import *


def h3_ocho_puzzle(estado):

    suc_ocho_puzzle = {0: 1, 1: 2, 2: 5, 3: 0, 4: 4, 5: 8, 6: 3, 7: 6, 8: 7}

    def secuencialidad_aux(estado, i):

        val=estado[i]
        if val == 0:
            return 0
        elif i == 4:
            return 1
        else:
            i_sig = suc_ocho_puzzle[i]
            val_sig = (val+1 if val<8 else 1)
            return 0 if val_sig == estado[i_sig] else 2

    def secuencialidad(estado):
        res = 0
        for i in range(8):
            res += secuencialidad_aux(estado, i)
        return res

    return h2_ocho_puzzle(estado) + 3*secuencialidad(estado)


# EXAMPLE:

print(h3_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5)))
