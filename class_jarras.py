from class_problema import *


class Jarras(Problema):

    def __init__(self):
        self.estado_inicial = (0,0)
#        super().__init__((0,0))

    def acciones(self,estado):
        jarra_de_4 = estado[0]
        jarra_de_3 = estado[1]
        accs = list()
        if jarra_de_4 > 0:
            accs.append("vaciar jarra de 4")
            if jarra_de_3 < 3:
                accs.append("trasvasar de jarra de 4 a jarra de 3")
        if jarra_de_4 < 4:
            accs.append("llenar jarra de 4")
            if jarra_de_3 > 0:
                accs.append("trasvasar de jarra de 3 a jarra de 4")
        if jarra_de_3 > 0:
            accs.append("vaciar jarra de 3")
        if jarra_de_3 < 3:
            accs.append("llenar jarra de 3")
        return accs

    def aplica(self, estado, accion):
        j4 = estado[0]
        j3 = estado[1]
        if accion == "llenar jarra de 4":
            return (4, j3)
        elif accion == "llenar jarra de 3":
            return (j4, 3)
        elif accion == "vaciar jarra de 4":
            return (0, j3)
        elif accion == "vaciar jarra de 3":
            return (j4,0)
        elif accion == "trasvasar de jarra de 4 a jarra de 3":
            return (j4-3+j3, 3) if j3+j4 >= 3 else (0, j3+j4)
        else:
            return (j3+j4, 0) if j3+j4 <= 4 else (4, j3-4+j4)

    def es_estado_final(self, estado):
        return estado[0] == 2

# EXAMPLE:


#pj = Jarras()
#print(pj.estado_inicial)
#print(pj.acciones(pj.estado_inicial))
#print(pj.aplica(pj.estado_inicial, "llenar jarra de 4"))
#print(pj.coste_de_aplicar_accion(pj.estado_inicial, "llenar jarra de 4"))
#print(pj.es_estado_final(pj.estado_inicial))





























