// Funcion para obtener el resultado de Puzzle_Lineal.py
function obtenerResultadoPuzzleLineal() {
    // Realizar la solicitud GET a la ruta de Flask
    fetch('/puzzle-lineal')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent = JSON.stringify(data.Resultado) // Mostrar la respuesta del servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });                                                                                                                               
}

// Funcion para obtener el resultado de Vuelos.py
function obtenerResultadoVuelos() {
    // Realizar la solicitud GET a la ruta de Flask
    fetch('/vuelos-en-amplitud')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent = JSON.stringify(data.Resultado) // Mostrar la respuesta del servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Funcion para obtener el resultado de DFS.py
function obtenerResultadoDFS() {
    // Realizar la solicitud GET a la ruta de Flask
    fetch('/dfs')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent = JSON.stringify(data.Resultado) // Mostrar la respuesta del servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Funcion para obtener el resultado de DFS_Recursivo.py
function obtenerResultadoDFSRecursivo() {
    // Realizar la solicitud GET a la ruta de Flask
    fetch('/busqueda-en-profundidad-recursivo')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent = JSON.stringify(data.Resultado) // Mostrar la respuesta del servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Funcion para obtener el resultado de DFS_Iterativo.py
function obtenerResultadoDFSIterativo() {
    // Realizar la solicitud GET a la ruta de Flask
    fetch('/busqueda-en-profundidad-iterativo')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent = JSON.stringify(data.Resultado) // Mostrar la respuesta del servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Funcion para obtener el resultado de Dijkstra.py
function obtenerResultadoDijkstra() {
    // Realizar la solicitud GET a la ruta de Flask
    fetch('/dijkstra')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent = JSON.stringify(data.Resultado) // Mostrar la respuesta del servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function obtenerResultadoTempladoSimulado() {
    // Realizar la solicitud GET a la ruta de Flask
    fetch('/templado-simulado')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent = JSON.stringify(data.Resultado) // Mostrar la respuesta del servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function obtenerResultadoHillClimbing() {
    // Realizar la solicitud GET a la ruta de Flask
    fetch('/hill-climbing')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent = JSON.stringify(data.Resultado) // Mostrar la respuesta del servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function obtenerResultadoHillClimbingIterativo() {
    // Realizar la solicitud GET a la ruta de Flask
    fetch('/hill-climbing-iterativo')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").textContent = JSON.stringify(data.Resultado) // Mostrar la respuesta del servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });
}