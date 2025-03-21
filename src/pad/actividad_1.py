import os
import sys
from tkinter.filedialog import Directory
import requests
import json

class Actividad_1:
    def __init__(self):
        ruta_actual = os.getcwd()  # Corregido

        self.ruta_static = "src/pad/static/".format(ruta_actual)
        self.ruta_json = "src/pad/static/json/".format(ruta_actual)
        Directory = os.path.dirname(self.ruta_json)
        if not os.path.exists(Directory):
            os.makedirs(Directory)
        sys.stdout.reconfigure(encoding="utf-8")

      
    def leer_api(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error {response.status_code} al acceder a la API"}

    def escribir_json(self, data, filename="output.json"):
        ruta_json = "{}json/{}".format(self.ruta_static,filename)
        with open(ruta_json, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

# Crear instancia de la clase
actividad = Actividad_1()

# URL de la API
url = "https://xeno-canto.org/api/2/recordings?query=cnt:brazil"

# Obtener datos de la API
datos_json = actividad.leer_api(url)

# Imprimir resultados
print(actividad.ruta_static)
print(json.dumps(datos_json, indent=4))

# Guardar los datos en un archivo JSON
actividad.escribir_json(datos_json)

