import requests

address = "La paz"
url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Esto lanza una excepción para códigos de estado HTTP de error
    data = response.json()
    if data:
        lat = data[0]['lat']
        lng = data[0]['lon']
        print(f"Latitud: {lat}, Longitud: {lng}")
    else:
        print("No se encontraron datos.")
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Error en la solicitud: {req_err}")
except requests.exceptions.JSONDecodeError as json_err:
    print(f"Error al decodificar el JSON: {json_err}")
