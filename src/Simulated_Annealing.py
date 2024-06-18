import math
import random

# Simulated Annealing para encontrar un camino entre dos ciudades usando conexiones
def distancia(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def evalua_ruta(ruta, coord, conexiones):
    total_distancia = 0
    for i in range(len(ruta) - 1):
        if ruta[i+1] in conexiones[ruta[i]]:
            total_distancia += conexiones[ruta[i]][ruta[i+1]]
        else:
            return float('inf')  # Si no existe conexión directa, retorna infinito
    return total_distancia

def genera_vecino(ruta, conexiones):
    n = len(ruta)
    while True:
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        if i != j and ruta[j] in conexiones[ruta[i]]:
            nueva_ruta = ruta[:]
            nueva_ruta[i], nueva_ruta[j] = nueva_ruta[j], nueva_ruta[i]
            return nueva_ruta

def simulated_annealing(origen, destino, conexiones, coord):
    # Crear una ruta inicial plausible
    ruta = [origen]
    while ruta[-1] != destino:
        siguientes = list(conexiones[ruta[-1]].keys())
        siguiente = random.choice(siguientes)
        if siguiente not in ruta:  # Evitar ciclos
            ruta.append(siguiente)

    T = 1000
    T_MIN = 1
    alpha = 0.95

    while T > T_MIN:
        nueva_ruta = genera_vecino(ruta, conexiones)
        costo_actual = evalua_ruta(ruta, coord, conexiones)
        nuevo_costo = evalua_ruta(nueva_ruta, coord, conexiones)
        if nuevo_costo < costo_actual or random.random() < math.exp((costo_actual - nuevo_costo) / T):
            ruta = nueva_ruta
        T *= alpha

    return ruta, evalua_ruta(ruta, coord, conexiones)

def main(capitales, conexiones):
    origen = input("Ingrese la ciudad de origen: ").upper()
    destino = input("Ingrese la ciudad de destino: ").upper()
    
    if origen not in capitales or destino not in capitales:
        print("Una o ambas ciudades ingresadas no se encuentran en las capitales disponibles.")
        return

    ruta_optima, distancia_total = simulated_annealing(origen, destino, conexiones, capitales)
    print("Ruta óptima:", ruta_optima)
    print("Distancia total:", distancia_total)

# Ejemplo de uso:
# main(capitales, conexiones)
