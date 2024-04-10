# Vuelos con Busqueda en Amplitud
from Arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_Visitados = []
    nodos_Frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_Frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_Frontera) !=0:
        nodo = nodos_Frontera[0]
        # Extraer nodo y añadirlos a visitados
        nodos_Visitados.append(nodos_Frontera.pop(0))
        if nodo.get_datos() == solucion:
            solucion = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo) # Aqui faltaba
                if not hijo.en_lista(nodos_Visitados) and not hijo.en_lista(nodos_Frontera):
                    nodos_Frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'CDMX': {'SLP', 'MEXICALI', 'CHIHUAHUA'},
        'ZAPOPAN': {'ZACATECAS', 'MEXICALI'},
        'GUADALAJARA': {'CHIAPAS'},
        'CHIAPAS': {'CHIHUAHUA'},
        'MEXICALI': {'SLP', 'ZAPOPAN', 'CDMX', 'CHIHUAHUA', 'SONORA'},
        'SLP': {'CDMX', 'MEXICALI'},
        'ZACATECAS': {'ZAPOPAN', 'SONORA', 'CHIHUAHUA'},
        'SONORA': {'ZACATECAS', 'MEXICALI'},
        'MICHOACAN': {'CHIHUAHUA'},
        'CHIHUAHUA': {'MICHOACAN', 'ZACATECAS', 'MEXICALI', 'CDMX', 'CHIAPAS'}
    }

estado_inicial = 'CDMX'
solucion = 'ZACATECAS'
nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

# Mostrar resultado
resultado = []
nodo = nodo_solucion
while nodo.get_padre() != None:
    resultado.append(nodo.get_datos())
    nodo = nodo.get_padre()

resultado.append(estado_inicial)
resultado.reverse()
print(resultado)

