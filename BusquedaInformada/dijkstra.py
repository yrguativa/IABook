# Dijkstra
import sys

def dijkstra(grafo,nodo_inicial):
    etiquetas ={}
    visitados=[]
    pendientes = [nodo_inicial] # es como la lista de nodos frontera
    nodo_actual = nodo_inicial

    # nodo inicial
    # Las etiquetas se guardan como {'1': [0,''] por ejemplo
    etiquetas[nodo_actual]= [0,'']

    # seleccionar el siguiente nodo de menor peso acumulado
    while len(pendientes)>0:
        nodo_actual= nodo_menor_peso(etiquetas,visitados)
        visitados.append(nodo_actual)

        # Obtener nodos adyacentes
        for adyacente , peso in grafo[nodo_actual].items():
            if adyacente not in pendientes and adyacente not in visitados:
                pendientes.append(adyacente)
            nuevo_peso=etiquetas[nodo_actual][0]+grafo[nodo_actual][adyacente] ##asigna peso sumando lo que lleva con la arista a recorrer

            # etiquetar
            if adyacente not in visitados:
                if adyacente not in etiquetas:
                    etiquetas[adyacente]=[nuevo_peso,nodo_actual]
                else:
                    if etiquetas[adyacente][0]> nuevo_peso: # si el peso nuevo es menor que el anterior
                        etiquetas[adyacente]= [nuevo_peso, nodo_actual]
        del pendientes[pendientes.index(nodo_actual)]
    return etiquetas

def nodo_menor_peso(etiquetas,visitados):
    menor =int(sys.maxsize)
    for nodo,etiqueta in etiquetas.items(): # separar la clave del diccionario de sus valores
        if etiqueta[0]<menor and nodo not in visitados:
            menor = etiqueta[0]
            nodo_menor=nodo # los contextos de las variables son mas randes que en java ( declaro dentro de un if y for y sirve aun fuera de ellos
    return nodo_menor

if __name__=='__main__':
    grafo={
        '1':{'3':6,'2':3},
        '2':{'4':1,'1':3,'3':2},
        '3':{'1':6,'2':2,'4':4,'5':2},
        '4':{'2':1,'3':4,'5':6},
        '5':{'3':2,'4':6,'6':2,'7':2},
        '6':{'5':2,'7':3},
        '7':{'5':2,'6':3}}
    etiquetas = dijkstra(grafo,'1')
    print(etiquetas)