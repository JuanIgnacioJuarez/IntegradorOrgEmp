import os
import requests
import time
from datetime import datetime
import pytz


# Obtener la clave API desde las variables de entorno
API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("No se ha proporcionado la clave API. Defina la variable de entorno 'API_KEY'.")

# Lista para almacenar el historial de consultas
historial = []

# Función para guardar la ciudad en el historial
def guardar_historial(nombre_ciudad, temp_min, temp_max, condiciones, fecha_consulta, unidad_temp):
    consulta = {
        "ciudad": nombre_ciudad,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "condiciones": condiciones,
        "fecha": fecha_consulta,
        "unidad": unidad_temp
    }
    historial.append(consulta)

# Función para mostrar el historial
def mostrar_historial():
    if historial:
        print("\nHistorial de consultas:")
        for i, consulta in enumerate(historial, 1):
            print(f"{i}. Ciudad: {consulta['ciudad']}")
            print(f"   Fecha de consulta: {consulta['fecha']}")
            print(f"   Condiciones: {consulta['condiciones']}")
            print(f"   Temperatura mínima: {consulta['temp_min']} {consulta['unidad']}")
            print(f"   Temperatura máxima: {consulta['temp_max']} {consulta['unidad']}\n")
    else:
        print("\nNo hay consultas en el historial.")
    input("Presione una tecla para continuar...")

# Función para obtener el clima de una ciudad
def obtener_clima(ciudad, unidades="metric"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units={unidades}&lang=es"
        
        inicio_tiempo = time.time()
        respuesta = requests.get(url)
        datos = respuesta.json()

        if respuesta.status_code == 200:
            nombre_ciudad = datos['name']
            temp_min = datos['main']['temp_min']
            temp_max = datos['main']['temp_max']
            humedad = datos['main']['humidity']
            condiciones = datos['weather'][0]['description']
            zona_argentina = pytz.timezone("America/Argentina/Buenos_Aires")
            fecha_consulta = datetime.now(zona_argentina).strftime("%Y-%m-%d %H:%M:%S")

            tiempo_respuesta = time.time() - inicio_tiempo
            if tiempo_respuesta <= 3:
                unidad_temp = "°C" if unidades == "metric" else "°F"
                print(f"\n--- Clima actual en {nombre_ciudad} ---")
                print(f"Condiciones: {condiciones}")
                print(f"Temperatura mínima: {temp_min}{unidad_temp}")
                print(f"Temperatura máxima: {temp_max}{unidad_temp}")
                print(f"Humedad: {humedad}%")
                print(f"Tiempo de respuesta: {tiempo_respuesta:.2f} segundos")
                
                # Guardar ciudad en el historial
                guardar_historial(nombre_ciudad, temp_min, temp_max, condiciones, fecha_consulta, unidad_temp)
            else:
                print("La respuesta tardó más de 3 segundos. Intente de nuevo.")
        else:
            print(f"Error: No se encontró la ciudad '{ciudad}'. Intente con una ciudad válida.")
    except requests.exceptions.RequestException:
        print("Error: No se pudo conectar con el servicio meteorológico. Verifique su conexión a internet.")
    input("Presione una tecla para continuar...")

# Función para obtener el pronóstico de 5 días
def obtener_pronostico(ciudad, unidades="metric"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={API_KEY}&units={unidades}&lang=es"
        respuesta = requests.get(url)
        datos = respuesta.json()

        if respuesta.status_code == 200:
            print(f"\n--- Pronóstico del clima en {ciudad} para los próximos 5 días ---")
            for pronostico in datos['list'][:5]:
                fecha = pronostico['dt_txt']
                temp = pronostico['main']['temp']
                descripcion = pronostico['weather'][0]['description']
                unidad_temp = "°C" if unidades == "metric" else "°F"
                print(f"{fecha}: {temp}{unidad_temp}, {descripcion}")
        else:
            print(f"Error: No se encontró la ciudad '{ciudad}'. Intente con una ciudad válida.")
    except requests.exceptions.RequestException:
        print("Error: No se pudo conectar con el servicio meteorológico. Verifique su conexión a internet.")
    input("Presione una tecla para continuar...")

# Función para iniciar la aplicación
def iniciar_aplicacion():
    unidades = "metric"  # Unidades por defecto: Celsius
    while True:
        print("\nOpciones:")
        print("1. Consultar clima actual")
        print("2. Cambiar unidades de medida (Celsius/Fahrenheit)")
        print("3. Ver historial de consultas")
        print("4. Ver pronóstico de 5 días")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            ciudad = input("\nIngrese el nombre de la ciudad: ")
            obtener_clima(ciudad, unidades)
        elif opcion == "2":
            vuelta = True
            while vuelta:
                unidad_input = input("Seleccione unidades (1. Celsius, 2. Fahrenheit): ")
                if unidad_input == "1":
                    unidades = "metric"
                    vuelta = False
                    print("Unidad cambiada a Celcius.")
                elif unidad_input == "2":
                    unidades = "imperial"
                    vuelta = False
                    print("Unidad cambiada a Fahrenheit.")
                else:
                    print("Opción no válida. Seleccione 1 o 2.")
            input("Presione una tecla para continuar...")
        elif opcion == "3":
            mostrar_historial()  # Llamamos correctamente a mostrar_historial()
        elif opcion == "4":
            ciudad = input("\nIngrese el nombre de la ciudad: ")
            obtener_pronostico(ciudad, unidades)
        elif opcion == "5":
            print("Gracias por usar la aplicación.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione una tecla para continuar...")

# Iniciar la aplicación
iniciar_aplicacion()