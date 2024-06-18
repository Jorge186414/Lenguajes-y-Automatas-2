# main.py
import folium
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


# Solicitar entrada del usuario
origen = input("Ingrese la capital de origen: ")
destino = input("Ingrese la capital de destino: ")

# Verificar que las capitales ingresadas existan en los datos
if origen not in capitales:
    print(f"Capital de origen '{origen}' no encontrada en los datos.")
elif destino not in capitales:
    print(f"Capital de destino '{destino}' no encontrada en los datos.")
else:
    camino, distancia = dijkstra(capitales, conexiones, origen, destino)
    if camino:
        print(f"La ruta más corta de {origen} a {destino} es: {camino} con una distancia de {distancia} km")
        # Crear el mapa centrado en la primera capital del camino
        mapa = folium.Map(location=capitales[camino[0]], zoom_start=6)

        # Añadir puntos al mapa
        for capital in camino:
            folium.Marker(location=capitales[capital], popup=capital).add_to(mapa)

        # Añadir líneas entre los puntos
        folium.PolyLine([capitales[capital] for capital in camino], color="blue", weight=2.5, opacity=1).add_to(mapa)

        # Guardar el mapa en un archivo HTML
        mapa.save("ruta_mas_corta.html")
        print("Mapa guardado como 'ruta_mas_corta.html'")
    else:
        print(f"No se encontró una ruta de {origen} a {destino}.")