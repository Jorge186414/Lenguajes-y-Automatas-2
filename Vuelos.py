# Vuelos con Busqueda en Amplitud
from Arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucon):
    solucionado = False
    nodos_Visitados = []
    nodos_Frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_Frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_Frontera) !=0:
        Nodo = nodos_Frontera[0]
        
        # Extraer nodo y añadirlos a visitados
        nodos_Visitados.append(nodos_Frontera.pop(0))