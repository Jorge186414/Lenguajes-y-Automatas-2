from flask import Flask, render_template, jsonify
import Puzzle_Lineal
import Vuelos
import DFS
import DFS_Recursivo
import DFS_Iterativo
import Dijkstra

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
    resultado_dfs_iterativo = DFS_Iterativo
    return jsonify({"Resultado": resultado_dfs_iterativo})

# Route a dijkstra
@app.route('/dijkstra', methods=['GET'])
def dijkstra():
    resultado_dijkstra = Dijkstra.imprimir()
    return jsonify({"Resultado": resultado_dijkstra})

if __name__ == '__main__':  
    app.run(debug=True)
