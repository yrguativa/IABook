# PLE con backtracking
def backtracking(variables, rango_variables, optimo, profundidad):
    min = rango_variables[profundidad][0]
    max = rango_variables[profundidad][1]
    for v in range(min, max):
        variables[profundidad] = v
        if profundidad < len(variables) - 1:
            # Es completable si no incumple ninguna restricción
            if es_completable(variables):
                optimo = backtracking(
                    variables[:], rango_variables, optimo, profundidad + 1)
            else:
                # Estamos en una hoja. Comprobamos solución
                sol = evalua_solucion(variables)
                if sol > evalua_solucion(optimo) and es_completable(variables):
                    optimo = (variables[0], variables[1])
    return optimo


def evalua_solucion(variables):
    x1 = variables[0]
    x2 = variables[1]
    val = (12-6) * x1 + (8-4) * x2
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
    rango_variables = [(0 , 51) , (0 , 76)]
    # mejor solución encontrada
    optimo = (0, 0)
    sol = backtracking(variables[:], rango_variables, optimo, 0)
    print("Mejor solución:")
    print(str(sol[0]) + " Pantalones.")
    print(str(sol[1]) + " Camisetas.")
    print("Beneficio: " + str(evalua_solucion(sol)))
