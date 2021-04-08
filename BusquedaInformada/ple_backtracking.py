# PLE con backtracking
def backtracking(variables, rango_variables, optimo, profundidad):
    min = rango_variables[profundidad][0]
    max = rango_variables[profundidad][1]
    for v in range(min, max):
        variables[profundidad] = v
        #estamos en el bloque de código para evaluar las ramas
        if profundidad < len(variables) -1:
            #Es completable si no incumple ninguna restricción
            if es_completable(variables):
                optimo = backtracking(variables[:], rango_variables, optimo, profundidad +1)
        #este bloque de código es para las hojas
        else:
            #comprobamos que la solucion sea optima para la hoja
            sol = evalua_solucion(variables)
            #si la solucion es mayor que optimo en su estado inicial y cumple que se puede completar con las restricciones dadas
            # entonces se asigna a optimo los valores actuales de la solucion
            if sol > evalua_solucion(optimo) and es_completable(variables):
                optimo = (variables[0], variables[1])
                
    return optimo

def evalua_solucion(variables):
    x1 = variables[0]
    x2 = variables[1]
    val = (12 - 6) * x1 + (8 - 4) * x2
    return val


def es_completable(variables):
    x1 = variables[0]
    x2 = variables[1]
    val1 = 7 * x1 + 4 * x2
    val2 = 6 * x1 + 5 * x2
    if val1 <= 150 and val2 <= 160:
        return True
    else:
        return False


if __name__ == "__main__":
    # valores de las variables x1 y x2
    variables = [0, 0]
    # rangos de las variables x1 y x2
    rango_variables = [(0, 51), (0, 76)]
    # mejor solucion encontrada
    optimo = (0, 0)
    sol = backtracking(variables[:], rango_variables, optimo, 0)
    print("Mejor solucion: ")
    print(str(sol[0]) + " Pantalones")
    print(str(sol[1]) + " Camisetas")
    print("Beneficio " + str(evalua_solucion(sol)))