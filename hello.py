from flask import Flask
from flask import render_template
import DFS

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dfs')
def dfs():
    return DFS.imprimir()
