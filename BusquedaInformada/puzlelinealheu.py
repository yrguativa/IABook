# Puzle Lineal con heurística

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from common.arbol import Nodo

def buscar_solucion_heuristica(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    else:
        # expandir nodos sucesores (hijos)
        dato_nodo = nodo_inicial.get_datos()
        hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_izquierdo = Nodo(hijo)
        hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_central = Nodo(hijo)
        hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_derecho = Nodo(hijo)
        nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

        for nodo_hijo in nodo_inicial.get_hijos():
            if not nodo_hijo.get_datos() in visitados and mejora(nodo_inicial, nodo_hijo):
                # llamada recursiva
                sol = buscar_solucion_heuristica(
                    nodo_hijo, solucion, visitados)
                if sol != None:
                    return sol
        return None

# función heurística:
# validad si el nodo hijo mejora respecto al padre en terminos de número de piezas mal colocadas
def mejora(nodo_padre, nodo_hijo):
    calidad_padre = 0
    calidad_hijo = 0
    dato_padre = nodo_padre.get_datos()
    dato_hijo = nodo_hijo.get_datos()
    for n in range(1, len(dato_padre)):
        if(dato_padre[n] > dato_padre[n-1]):
            calidad_padre = calidad_padre + 1
        if (dato_hijo[n] > dato_hijo[n-1]):
            calidad_hijo = calidad_hijo + 1

    if calidad_hijo >= calidad_padre:
        return True
    else:
        return False


if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = None
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodo = buscar_solucion_heuristica(nodo_inicial, solucion, visitados)

    # mostrar resultado
    resultado = []
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()

    print(resultado)
