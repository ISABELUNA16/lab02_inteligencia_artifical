from simpleai.search import astar, SearchProblem


# Busqueda en Profundidad


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


def find_location(rows, element_to_find):
    '''Encuentra la direccion de la ficha buscada, devuelve la tupla fila, columna'''
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


GOAL = '''1-2-3
4-5-6
7-8-e'''
goal_positions = {}
rows_goal = string_to_list(GOAL)
for number in '12345678e':
    goal_positions[number] = find_location(rows_goal, number)


class EigthPuzzleProblem(SearchProblem):
    def actions(self, state):
        '''Retorna una lista de las piezas que podemso mover a un espacio vacio'''
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')

        actions = []
        if row_e > 0:
            actions.append(rows[row_e - 1][col_e])
        if row_e < 2:
            actions.append(rows[row_e + 1][col_e])
        if col_e > 0:
            actions.append(rows[row_e][col_e - 1])
        if col_e < 2:
            actions.append(rows[row_e][col_e + 1])

        return actions

    def result(self, state, action):
        '''retorna el estado resultante despues de mover una ficha a un espacio vacio.
           (La accion parameter contiene la pieza a mover)
        '''
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')
        row_n, col_n = find_location(rows, action)

        rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]

        return list_to_string(rows)

    def is_goal(self, state):
        '''Devuelve true si el estado actual es el estado deseado'''
        return state == GOAL

    def heuristic(self, state):
        '''Retorna una estimacion de la distancia al estado deseado
           Usando la distancia manhatan
        '''
        rows = string_to_list(state)

        distance = 0

        for number in '12345678e':
            row_n, col_n = find_location(rows, number)
            row_n_goal, col_n_goal = goal_positions[number]

            distance += abs(row_n - row_n_goal) + abs(col_n - col_n_goal)

        return distance


INITIAL = '''1-6-7
5-8-3
4-e-2'''

# result = astar(EigthPuzzleProblem(INITIAL))


# for action, state in result.path():
#    print('Mover el numero ', action)
#    print(state)
