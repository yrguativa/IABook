#viaje por carretera con búsqueda A*
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from common.arbol import Nodo
from math import sin, cos, acos

def compara(x):
    #g(n) + h(n) para ciudad x
    lat1 = coord[x.get_datos()][0]
    lon1 = coord[x.get_datos()][1]
    lat2 = coord[solucion][0]
    lon2 = coord[solucion][1]
    d = int(geodist(lat1, lon1, lat2, lon2))
    c1 = x.get_coste() + d
    return c1

def geodist(lat1, lon1, lat2, lon2):
    grad_rad = 0.01745329
    rad_grad = 57.29577951
    longitud = lon1 - lon2
    val = (sin(lat1*grad_rad)*sin(lat2*grad_rad) + cos(lat1*grad_rad)*cos(lat2*grad_rad)*cos(longitud*grad_rad))
    return (acos(val)*rad_grad)*111.32

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        #ordenar la lista de nodos_frontera
        nodo_frontera = sorted (nodos_frontera, key=compara)
        nodo = nodos_frontera[0]
        #extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            #solucion encontrada
            solucionado = True
            return nodo
        else:
            #expandir nodos hijo (ciudades con conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                #cálculo g(n): coste acumulado
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    #si esta en la lista lo sustituimos con 
                    # el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
            nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'Malaga': {'Granada':125, 'Madrid':513},
        'Sevilla': {'Madrid':514},
        'Granada': {'Malaga':125, 'Madrid':423, 'Valencia':491},
        'Valencia': {'Granada': 491, 'Madrid':356, 'Zaragoza':309, 'Barcelona':346},
        'Madrid': {'Salamanca':203, 'Sevilla':514, 'Malaga':513, 'Granada':423,'Barcelona':603, 'Santander':437, 'Valencia':356, 'Zaragoza':313, 'Santander':437, 'Santiago':599},
        'Salamanca': {'Santiago':390, 'Madrid':203},
        'Santiago': {'Salamanca':390, 'Madrid':599},
        'Santander': {'Madrid':437, 'Zaragoza':394},
        'Zaragoza': {'Barcelona':296, 'Valencia':309, 'Madrid':313},
        'Barcelona': {'Zaragoza':296, 'Madrid':603, 'Valencia':346}
    }

    coord = {
        'Malaga': (36.43, -4.24),
        'Sevilla': (37.23, -5.59),
        'Granada': (37.11, -3.35),
        'Valencia': (39.28, -0.22),
        'Madrid': (40.24, -3.41),
        'Salamanca': (40.57, -5.40),
        'Santiago': (42.52, -8.33),
        'Santander': (43.28, -3.48),
        'Zaragoza': (41.39, -0.52),
        'Barcelona': (41.23, 2.11)
    }

    estado_inicial = 'Malaga'
    solucion = 'Santiago'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
    #mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)