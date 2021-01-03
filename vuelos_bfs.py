# Vuelos con búsqueda en amplitud 
from arbol import Nodo

def  buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while  (not solucionado ) and len(nodos_frontera) != 0:
        nodo =  nodos_frontera[0] 
        # extraer nodo y anadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # solución encotrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) and \
                 not  hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'Malaga':{'Dalamanca','Madrid', 'Barcelona'},
        'Sevilla':{'Santigao', 'Madrid'},
        'Granada':{'Valencia'},
        'Valencia':{'Barcelona'},
        'Madrid':{'Sañamanca','Sevilla','Malaga', 'Barcelona','Santander'},
        'Salamanca':{'Malaga','Madrid'},
        'Santiago':{'Sevilla', 'Santander','Barcelona'},
        'Sntander':{'Dantiago','Madrid'},
        'Zaragoza':{'Barcelona'},
        'Barcelona':{'Zaragoza','Santiago','Madrid','Malaga','Valencia'}
    }
    estado_inicial ='Malaga'
    solucion = 'Santiago'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

    # mostrar resultado
    resultado = []
    nodo= nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    