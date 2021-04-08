# Búsqueda Informada

Algunos problemas, ofrecen información que podemos usar para mejorar la búsqueda llevandonos más directamente a la solución buscada, esto lo logra recorriendo el arbol por ramas que parecen más prometedoras

## Función Heurística
h(n) trata de guiar la búsqueda para llegar de forma más rápida a la solución, apartir de la información disponible. Intentado estimar el coste del menor camino (mejor coste) desde el nodo n hasta el nodo objetivo.

La función heurística h(n) depende  únicamente del nodod que se está analizando en ese momento.

> NOTA: La eleción de una buena función heurísticaes crucial para obtener una buena solución.

## Búsqueda con vuelta atrás (Backtracking)
Mejora la busqueda en profundidad usando una función heurística, lo hacemos al momento de validad si el nodo hijo empeora la situación y como no tiene sentido seguir explorando una rama por se **no completable**, o que hacemos es que dejamos de explorar y volvemos hacia atrás