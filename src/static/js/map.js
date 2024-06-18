let map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: { lat: 23.6345, lng: -102.5528 }, // Centra el mapa en México
    });
}

$(document).ready(function () {
    $('#route-form').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            url: '/',
            type: 'POST',
            data: $(this).serialize(),
            success: function (response) {
                const rutaCoords = response.ruta_coords.map(coord => ({ lat: coord[0], lng: coord[1] }));
                const path = new google.maps.Polyline({
                    path: rutaCoords,
                    geodesic: true,
                    strokeColor: '#FF0000',
                    strokeOpacity: 1.0,
                    strokeWeight: 2,
                });
                path.setMap(map);

                // Centrar el mapa en la primera coordenada del camino
                map.setCenter(rutaCoords[0]);

                // Añadir marcadores
                rutaCoords.forEach((coord, index) => {
                    new google.maps.Marker({
                        position: coord,
                        map: map,
                        title: `Punto ${index + 1}`,
                    });
                });
            },
            error: function (xhr) {
                alert(xhr.responseText);
            }
        });
    });
});
