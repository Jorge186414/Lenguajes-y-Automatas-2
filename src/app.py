from flask import Flask, render_template, jsonify
import Puzzle_Lineal
import Vuelos
import DFS
import DFS_Recursivo
import DFS_Iterativo
import Dijkstra
import Hill_Climbing
import Hill_Climbing_Iterativo
import Simulated_Annealing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route a Puzzle_Lineal.py
@app.route('/puzzle-lineal', methods=['GET'])
def puzzle_Lineal():
    resultado_puzzle_lineal = Puzzle_Lineal.imprimir()
    return jsonify({"Resultado": resultado_puzzle_lineal})

# Route a Vuelos
@app.route('/vuelos-en-amplitud', methods=['GET'])
def vuelos_Amplitud():
    resultado_vuelos_amplitud= Vuelos.imprimir()
    return jsonify({"Resultado": resultado_vuelos_amplitud})

# Route a DFS
@app.route('/dfs', methods=['GET'])
def dfs():
    resultado_dfs = DFS.imprimir()
    return jsonify({"Resultado": resultado_dfs})

# Route a DFS recursivo
@app.route('/busqueda-en-profundidad-recursivo', methods=['GET'])
def dfs_Recursivo():
    resultado_dfs_recursivo = DFS_Recursivo.imprimir()
    return jsonify({"Resultado": resultado_dfs_recursivo})

# Route a DFS iterativo
@app.route('/busqueda-en-profundidad-iterativo', methods=['GET'])
def dfs_Iterativo():
    resultado_dfs_iterativo = DFS_Iterativo.imprimir()
    return jsonify({"Resultado": resultado_dfs_iterativo})

# Route a dijkstra
@app.route('/dijkstra', methods=['GET'])
def dijkstra():
    resultado_dijkstra = Dijkstra.imprimir()
    return jsonify({"Resultado": resultado_dijkstra})

@app.route('/hill-climbing', methods=['GET'])
def hillClimbing():
    resultado_hill_climbing = Hill_Climbing.imprimir()
    return jsonify({"Resultado": resultado_hill_climbing})

@app.route('/hill-climbing-iterativo', methods=['GET'])
def hillClimbingIterativo():
    resultado_hill_climbing_iterativo = Hill_Climbing_Iterativo.imprimir()
    return jsonify({"Resultado": resultado_hill_climbing_iterativo})

# Route a templado simulado
@app.route('/templado-simulado', methods=['GET'])
def allin():
    resultado_templado = Simulated_Annealing.simu()
    return jsonify({"Resultado": resultado_templado})

if __name__ == '__main__':  
    app.run(debug=False)
