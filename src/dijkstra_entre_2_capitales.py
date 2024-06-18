# main.py

import heapq
from datos import capitales, conexiones

def dijkstra(capitales, conexiones, inicio, fin):
    # Inicialización
    distancias = {capital: float('inf') for capital in capitales}
    distancias[inicio] = 0
    predecesores = {capital: None for capital in capitales}
    pq = [(0, inicio)]
    
    while pq:
        distancia_actual, capital_actual = heapq.heappop(pq)
        
        if distancia_actual > distancias[capital_actual]:
            continue
        
        for vecino, peso in conexiones[capital_actual].items():
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesores[vecino] = capital_actual
                heapq.heappush(pq, (distancia, vecino))
    
    # Reconstrucción del camino
    camino = []
    capital = fin
    while capital is not None:
        camino.append(capital)
        capital = predecesores[capital]
    
    camino.reverse()
    return camino, distancias[fin]

# Ejemplo de uso
inicio = 'CHIHUAHUA'
fin = 'TOLUCA_DE_LERDO'
camino, distancia = dijkstra(capitales, conexiones, inicio, fin)
print(f"La ruta más corta de {inicio} a {fin} es: {camino} con una distancia de {distancia} km")
