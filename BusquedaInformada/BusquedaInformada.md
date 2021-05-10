# Búsqueda Informada

Algunos problemas, ofrecen información que podemos usar para mejorar la búsqueda llevandonos más directamente a la solución buscada, esto lo logra recorriendo el arbol por ramas que parecen más prometedoras

## Función Heurística
h(n) trata de guiar la búsqueda para llegar de forma más rápida a la solución, apartir de la información disponible. Intentado estimar el coste del menor camino (mejor coste) desde el nodo n hasta el nodo objetivo.

La función heurística h(n) depende  únicamente del nodod que se está analizando en ese momento.

> NOTA: La eleción de una buena función heurísticaes crucial para obtener una buena solución.

## Búsqueda con vuelta atrás (Backtracking)
Mejora la busqueda en profundidad usando una función heurística, lo hacemos al momento de validad si el nodo hijo empeora la situación y como no tiene sentido seguir explorando una rama por se **no completable**, o que hacemos es que dejamos de explorar y volvemos hacia atrás

## Algoritmo A* (A estrella)
Hace uso de una funcion heurística h(n) wue trata de estimar el coste desde el nodo n hasta el nodo objetivo, para reducir el alto precio que se puede presentar en la búsqueda de coste.
La función de evaluación : Usa la suma del coste acumulador desde el nodo raíz mas el coste estimado hasta el nodo solución.
```
f(n) = g(n) + h(n)
```
[Código](https://github.com/yrguativa/IABook/blob/master/BusquedaInformada/ple_backtracking.py)
## Búsqueda local (grredy)
Tratan de mejorar una solución de forma iterativa, haciendo pequeñas modificaciones sobre una solución inicial en cada iteración, siempre y cuando no se viole ninguna de las restricciones del problema.

> NOTA: La búsqueda local se utiliza en problemas en los que nos iteresa el resultado y no las acciones necesarias para llegar a él.

Al estado resultante tras aplicarle el cambio lo denominamos **estado vecino**. Al aplicar los operadores para obtener los vecinos de un estado se debe tener en cuenta las restriciones. Estás pueden surgir por el enunciado del problema o bien derivarse de la naturaleza del propio problema. Al proceso de comprobar si el vecino es una solución.

## Algoritmos constructivos voraces
Son aquellos que utilizan una función heurística consistente en elegir la mejor opciónen cada paso para ir construtendo una solución.

> NOTA: Suelen usarse para generar soluciones iniciales.

