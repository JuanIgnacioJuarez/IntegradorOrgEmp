import os
import requests
import time

# Obtener la clave API desde las variables de entorno
API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("No se ha proporcionado la clave API. Defina la variable de entorno 'API_KEY'.")


def obtener_clima(ciudad):
    try:
        # URL para la solicitud a la API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
        
        # Registramos el tiempo de inicio para medir el tiempo de respuesta
        inicio_tiempo = time.time()
        
        # Realizamos la solicitud GET a la API
        respuesta = requests.get(url)
        datos = respuesta.json()

        # Verificamos si la ciudad es válida
        if respuesta.status_code == 200:
            # Información meteorológica
            nombre_ciudad = datos['name']
            temp_min = datos['main']['temp_min']
            temp_max = datos['main']['temp_max']
            humedad = datos['main']['humidity']
            condiciones = datos['weather'][0]['description']

            # Calculamos el tiempo de respuesta
            tiempo_respuesta = time.time() - inicio_tiempo

            # Si el tiempo de respuesta es menor de 3 segundos, mostramos los datos
            if tiempo_respuesta <= 3:
                print(f"\n--- Clima actual en {nombre_ciudad} ---")
                print(f"Condiciones: {condiciones}")
                print(f"Temperatura mínima: {temp_min}°C")
                print(f"Temperatura máxima: {temp_max}°C")
                print(f"Humedad: {humedad}%")
                print(f"Tiempo de respuesta: {tiempo_respuesta:.2f} segundos")
            else:
                print("La respuesta tardó más de 3 segundos. Intente de nuevo.")
        else:
            print(f"Error: No se encontró la ciudad '{ciudad}'. Intente con una ciudad válida.")

    except requests.exceptions.RequestException:
        print("Error: No se pudo conectar con el servicio meteorológico. Verifique su conexión a internet.")

def iniciar_aplicacion():
    while True:
        ciudad = input("\nIngrese el nombre de la ciudad (o 'salir' para terminar): ")

        if ciudad.lower() == "salir":
            print("Gracias por usar la aplicación.")
            break

        obtener_clima(ciudad)

# Iniciar la aplicación
iniciar_aplicacion()
