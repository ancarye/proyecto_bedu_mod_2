import requests

url = 'https://pokeapi.co/api/v2/pokemon/'

response = requests.get(url)

print(response)

data=response.json()

print(data)

# Nombre de cada pokemon


name = (data['results'])
i = 0

for names, value in name:
    pokemon = (data['results'][i]['name'])
    print(pokemon)
    i=i+1

import os
import requests
from PIL import Image
from io import BytesIO

# URL base de la API que contiene la información de los Pokémon
base_url = 'https://pokeapi.co/api/v2/pokemon/'

# Solicitar al usuario que ingrese el nombre del Pokémon
pokemon_name = input("Por favor ingresa el nombre del Pokémon: ").lower()

# URL completa del Pokémon
pokemon_url = f'{base_url}{pokemon_name}'

# Realizar la solicitud a la API
response = requests.get(pokemon_url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a JSON
    data = response.json()

    # Obtener la URL de la imagen desde el JSON
    image_url = data['sprites']['front_default']

    # Realizar una solicitud para obtener la imagen
    image_response = requests.get(image_url)

    # Verificar si la solicitud de la imagen fue exitosa
    if image_response.status_code == 200:
        # Convertir la imagen de bytes a objeto de imagen
        image = Image.open(BytesIO(image_response.content))

        # Ruta de la carpeta temporal dentro del proyecto de Visual Studio
        project_temp_dir = os.path.join(os.getcwd(), 'temp')

        # Guardar la imagen en formato PNG en la carpeta temporal del proyecto
        file_path = os.path.join(project_temp_dir, f'{pokemon_name}_image.png')
        image.save(file_path, format='PNG')

        print(f"La imagen de {pokemon_name.capitalize()} ha sido guardada en: {file_path}")
    else:
        print("No se pudo obtener la imagen del Pokémon.")
else:
    print("No se pudo obtener la información del Pokémon.")