# Algoritmos de búsqueda en espacios de estados

# El código que se usa en esta práctica está basado principalmente en el
# código Python que se proporciona con el libro "Artificial Intelligence: A
# Modern Approach" de S. Russell y P. Norvig
# (http://code.google.com/p/aima-python, módulo search.py).

# --------------------------------------------
# Auxiliar: colas, pilas y colas con prioridad
# --------------------------------------------

import bisect
# Necesario para las listas con prioridad


class Cola:
    """Clase abstracta/interfaz para colas de tres tipos:
        PilaLIFO(): Pilas
        ColaFIFO(): Colas.
        ColaPrioridad(orden, f): Colas ordenadas según f.
    Cualquiera de ellos soporta los siguientes métodos y funciones:
        q.append(item)  -- incluir un elemento en la cola q
        q.extend(items) -- equivalente a: for x in items: q.append(x)
        q.pop()         -- devuelve (y lo quita) el primero de la cola
        len(q)          -- número de elementos en q
        item in q       -- responde a la pregunta ¿item está en q?

    En el caso particular de PilaLIFO(), no será una instance de Cola, ya que
    directamente usaremos listas. Las otras dos sí serán definidas como
    subclase de esta clase Cola."""

    def __init__(self):
        abstract

    def extend(self, items):
        for item in items: self.append(item)


def PilaLIFO():
    """Devuelve la lista vacía, que tomaremos como una pila LIFO vacía."""
    return []


class ColaFIFO(Cola):
    """Definición de colas 'primero que entra, primero que sale'. Se usan listas y la cola que representan es la que se forma si se recorre la lista
    de izquierda a derecha. Para eliminar un elemento de la cola, simplemente consideramos que el inicio de la cola cambia a la siguiente posición a la
    derecha. Para ello, llevamos un contador con el índice que indica el comienzo de la cola, y lo incrementaremos cuando se hace pop().  A partir de
    cinco, eliminamos la "basura" cuando más de la mitad de la lista esté eliminada (para ello, reemplazamos la lista por la sublista de los
    elementos "vivos")."""

    def __init__(self):
        self.A = []
        self.comienzo = 0

    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.comienzo

    def extend(self, items):
        self.A.extend(items)

    def pop(self):
        e = self.A[self.comienzo]
        self.comienzo += 1
        if self.comienzo > 5 and self.comienzo > len(self.A)/2:
            self.A = self.A[self.comienzo:]
            self.comienzo = 0
        return e

    def __contains__(self, item):
        return item in self.A[self.comienzo:]

    def __str__(self):
        return str(self.A[self.comienzo:])


class ColaPrioridad(Cola):
    """Cola ordenada respecto a un valor dado por una función f, que la clase tiene como atributo de dato. Admite orden creciente (min) y orden
    decreciente (max). Si el orden es min, el método pop devuelve y elimina el elemento de la cola con menor f(x). Si el orden es max, devuelve y elimina
    el de mayor f(x). En realidad, los elementos quie se guardan en la cola son tuplas (f(x),x). En Python, las tuplas se comparan lexicográficamente,
    así que se mantendrán ordenadas por su valor f(x). La pertenencia a la cola (x in C) se comprueba con x e ignorando f(x). Soporta además acceso
    como en diccionarios, ignorando igualmente el valor de f(x)"""

    def __init__(self, orden=min, f=lambda x: x):
        self.A=[]
        self.orden=orden
        self.f=f

    def append(self, item):
        bisect.insort(self.A, (self.f(item), item))

    def __len__(self):
        return len(self.A)

    def pop(self):
        if self.orden == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]

    def __contains__(self, item):
        for (_, x) in self.A:
            if x == item: return True
        return False

    def __getitem__(self, clave):
        for _, item in self.A:
            if item == clave:
                return item

    def __delitem__(self, clave):
        for i, (valor, item) in enumerate(self.A):
            if item == clave:
                self.A.pop(i)
                return

    def __str__(self):
        return str(self.A)



# -----------------
# Nodos de búsqueda
# -----------------

# Según lo visto en clase, la generación de los aŕboles de búsqueda en
# espacios de estado se hace a través de lo que llamamos nodo de búsqueda. La
# siguiente clase implementa los nodos de búsqueda:

class Nodo:
    """Nodos de un árbol de búsqueda. Un nodo se define como:
       - Un estado
       - Un puntero al estado desde el que viene (padre)
       - La acción que se ha aplicado al padre para que se obtenga el
         estado del nodo
       - Profundidad del nodo
       - Coste del camino desde el estado inicial hasta el nodo.

       Definimos además, entre otros, los siguientes métodos que se
       necesitarán para generar el aŕbol de búsqueda:
       - Sucesor y sucesores de un nodo (respesctivamente por una acción
         o por todas las acciones aplicables al estado del nodo). Estos
         métodos reciben como entrada un  problema de espacio de estados.
       - Camino (secuencia de nodos) que lleva del estado inicial al estado del
         nodo.
       - Solución (secuencia de acciones que llevan al estado) de un nodo.
       """

    def __init__(self, estado, padre=None, accion=None, coste_camino=0):
        self.estado=estado
        self.padre=padre
        self.accion=accion
        self.coste_camino=coste_camino
        self.profundidad=0
        if padre:
            self.profundidad= padre.profundidad + 1

    def __repr__(self):
        return "<Nodo {0}>".format(self.estado)

    def sucesor(self, problema, accion):
        """Sucesor de un nodo por una acción aplicable"""
        estado_suc = problema.aplica(self.estado, accion)
        return Nodo(estado_suc, self, accion,
                    problema.coste_de_aplicar_accion(self.estado,accion)+self.coste_camino)

    def sucesores(self, problema):
        """Lista de los nodos sucesores por todas las acciones que le sean
           aplicables"""
        return [self.sucesor(problema, accion)
                for accion in problema.acciones(self.estado)]

    def camino(self):
        """Lista de nodos que forman el camino desde el inicial hasta el
           nodo."""
        nodo_aux, camino_inverso = self, []
        while nodo_aux:
            camino_inverso.append(nodo_aux)
            nodo_aux = nodo_aux.padre
        return list(reversed(camino_inverso))

    def solucion(self):
        """Secuencia de acciones desde el nodo inicial"""
        return [nodo.accion for nodo in self.camino()[1:]]

    def __eq__(self, other):
        """ Dos nodos son iguales si sus estados son iguales. Esto significa que
        cuando comprobemos pertenecia a una lista o a un conjunto (con"in"), sólo
        miramos los estados. Si hay que nirar, por ejemplo, algo del coste,
        habrá que hacerlo expresamente, como se hará en la
        buśqueda_con_prioridad"""

        return isinstance(other, Nodo) and self.estado == other.estado

    def __lt__(self, other):
        """La definición del menor entre nodos se necesita porque cuando se
        introduce un nodo en la cola de prioridad, con la misma valoración que
        uno ya existente, se van a comparar los nodos y por tanto es necesario que
        esté definido el operador <"""
        return True

    def __hash__(self):
        """Nótese que esta definición obliga a que los estados sean de un tipo
        de dato hashable"""
        return hash(self.estado)

# ------------------------------
# Algoritmo genérico de búsqueda
# ------------------------------


def busqueda_generica(problema, abiertos):
    """Búsqueda genérica, tal y como se ha visto en clase; aquí
    abiertos es una cola que se puede gestionar de varias maneras.
    Cuando se llama a la función, el argumento abiertos debe ser la cola
    vacía.
    Téngase en cuenta que en esta búsqueda, para ver si se repite un nodo,
    sólo se mira el estado. Por tanto, las búsquedas que usan coste (coste uniforme o
    A*, por ejemplo), no se pueden obtener como caso particular de ésta (serán
    casos particulares de búsqueda_con_prioridad)"""


    abiertos.append(Nodo(problema.estado_inicial))
    cerrados = set()
    while abiertos:
        actual = abiertos.pop()
        if problema.es_estado_final(actual.estado):
            return actual
        cerrados.add(actual.estado)
        nuevos_sucesores=(sucesor for sucesor in actual.sucesores(problema)
                          if sucesor.estado not in cerrados
                          and sucesor not in abiertos)
        abiertos.extend(nuevos_sucesores)
    return None


# -------------------------------------
# Búsquedas en anchura y en profundidad
# -------------------------------------

# Usando la búsqueda genérica, se pueden implementar los algoritmos
# búsqueda_en_anchura y búsqueda_en_profundidad.



def busqueda_en_profundidad(problema):
    return busqueda_generica(problema, PilaLIFO())


def busqueda_en_anchura(problema):
    return busqueda_generica(problema, ColaFIFO())



# -------------------------------
# Búsqueda genérica con prioridad
# -------------------------------


# La siguiente función búsqueda_con_prioridad(problema,f), define una búsqueda
# genérica en la que la cola de abiertos se gestiona como una cola con
# prioridad, ordenándo los nodos de menor a mayor valoración según una función
# dada f. Nótese que la búsqueda por primero el mejor, la búsqueda óptima y la
# búsqueda A* pueden verse como casos particulares de esta búsqueda, usando
# distintas funciones "f".

# Esta búsqueda con prioridad varía respecto a la búsqueda genérica anterior,
# en un detalle. Si se genera un nodo cuyo estado ya está en un nodo de
# abiertos pero con mayor coste, ha de ser incluidos en abiertos.

def busqueda_con_prioridad(problema, f):
    """Búsqueda que gestiona la cola de abiertos ordenando los nodos de menor
    a mayor valor de f. Tanto la búsqueda por primero el mejor, como la
    búsqueda óptima y la búsqueda A* son casos particulares de esta búsqueda,
    usando distintas f's (heurística, coste y coste más heurística,
    respectivamente)."""

    actual = Nodo(problema.estado_inicial)
    if problema.es_estado_final(actual.estado):
        return actual
    abiertos = ColaPrioridad(min, f)
    abiertos.append(actual)
    cerrados = set()
    while abiertos:
        actual = abiertos.pop()
        if problema.es_estado_final(actual.estado):
            return actual
        cerrados.add(actual.estado)
        for sucesor in actual.sucesores(problema):
            if sucesor.estado not in cerrados and sucesor not in abiertos:
                abiertos.append(sucesor)
            elif sucesor in abiertos:
                nodo_con_mismo_estado = abiertos[sucesor]
                if f(sucesor) < f(nodo_con_mismo_estado):
                    del abiertos[nodo_con_mismo_estado]
                    abiertos.append(sucesor)
    return None



# ---------------------------------------
# Búsquedas óptima, primero el mejor y A*
# ---------------------------------------

# Usando la búsqueda con prioridad definida anteriormente, implementamos los
# algoritmos búsqueda_óptima, búsqueda_primero_el_mejor y
# búsqueda_a_estrella. Nótese que los dos últimos algoritmos, además del
# problema, reciben como entrada la función heurística que han de utilizar


def busqueda_coste_uniforme(problema):
    """Busqueda óptima: gestiona la cola en orden creciente de coste del camino"""
    return busqueda_con_prioridad(problema, lambda x: x.coste_camino)


def busqueda_primero_el_mejor(problema, h=None):

    """Búsqueda por primero el mejor: gestionar la cola de menor a mayor
    heurística.
    NOTA: en realidad, al hacer que primero_el_mejor sea un caso
    particular de búsqueda_con_prioridad, estamos poniendo en este algoritmo
    un test innecesario. Cuando el estado de un nodo generado es el mismo que
    el del un nodo que está en abiertos o en cerrados, su valoración (su
    heurística en este caso) es la misma que el nodo que ya está en la lista,
    ya que la heurística sólo depende del estado. Sin embargo,
    búsqueda_con_prioridad comprueba si su valoración es menor o no (en este
    caso inútilmente). Hemos preferido dejarlo así para enfatizar la
    estructura común de estos algoritmos"""

    return busqueda_con_prioridad(problema,lambda n: h(n.estado))


def busqueda_a_estrella(problema, h=None):
    """A*: la cola se ordena por f(n) = g(n)+h(n) (coste más heurística)."""

    return busqueda_con_prioridad(problema,lambda n: n.coste_camino + h(n.estado))
