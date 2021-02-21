# Búsqueda con Coste Uniforme - Uniform Cost Search
from arbol import Nodo


# def compara(x, y):
#     return x.get_coste() - y.get_coste()

def compara(node):
    return node.get_coste()


def search_solution_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        # Ordenar lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key=compara)
        nodo = nodos_frontera[0]
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijo (ciudades con conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # Si está en la lista lo sustituimos con el nuevo valor de coste si es menor
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
        'Malaga': {'Granada': 125, 'Madrid': 513},
        'Sevilla': {'Madrid': 514},
        'Granada': {'Malaga': 125, 'Madrid': 423, 'Valencia': 491},
        'Valencia': {'Granada': 491, 'Madrid': 356, 'Zaragoza': 309, 'Barcelona': 346},
        'Madrid': {'Salamanca': 203, 'Sevilla': 514, 'Malaga': 513, 'Granada': 423, 'Barcelona': 603, 'Santander': 437,
                   'Valencia': 356, 'Zaragoza': 313, 'Santiago': 599},
        'Salamanca': {'Santiago': 390, 'Madrid': 203},
        'Santiago': {'Salamanca': 390, 'Madrid': 599},
        'Santander': {'Madrid': 437, 'Zaragoza': 394},
        'Zaragoza': {'Barcelona': 296, 'Valencia': 309, 'Madrid': 313},
        'Barcelona': {'Zaragoza': 296, 'Madrid': 603, 'Valencia': 396}
    }
    estado_inicial = 'Malaga'
    solucion = 'Santiago'
    nodo_solucion = search_solution_UCS(conexiones, estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    Nodo = nodo_solucion
    while Nodo.get_padre() is not None:
        resultado.append(Nodo.get_datos())
        Nodo = Nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Coste: %s" % str(nodo_solucion.get_coste()))
