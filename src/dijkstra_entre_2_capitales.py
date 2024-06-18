from flask import Flask, render_template, request, jsonify
import heapq
from datos import capitales, conexiones

app = Flask(__name__)

def dijkstra(capitales, conexiones, inicio, fin):
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
    
    camino = []
    capital = fin
    while capital is not None:
        camino.append(capital)
        capital = predecesores[capital]
    
    camino.reverse()
    return camino, distancias[fin]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        inicio = data['inicio']
        fin = data['fin']

        if inicio not in capitales:
            return jsonify({"error": f"Capital de origen '{inicio}' no encontrada en los datos."}), 400
        elif fin not in capitales:
            return jsonify({"error": f"Capital de destino '{fin}' no encontrada en los datos."}), 400
        else:
            camino, distancia = dijkstra(capitales, conexiones, inicio, fin)
            if camino:
                ruta_coords = [capitales[capital] for capital in camino]
                return jsonify({'ruta_coords': ruta_coords, 'distancia': distancia})
            else:
                return jsonify({"error": f"No se encontró una ruta de {inicio} a {fin}."}), 400

    return render_template('index.html', cities=list(capitales.keys()))

if __name__ == '__main__':
    app.run(debug=True)
