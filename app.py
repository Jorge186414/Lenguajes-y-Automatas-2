from flask import Flask, render_template, jsonify
import Puzzle_Lineal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/puzzle-lineal', methods=['GET'])
def dfs():
    resultado_puzzle_lineal = Puzzle_Lineal.imprimir()
    return jsonify({"Resultado": resultado_puzzle_lineal})

if __name__ == '__main__':  
    app.run(debug=True)
