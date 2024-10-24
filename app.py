import os
from menu import mostrar_menu

# Obtener la clave API desde las variables de entorno
API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("No se ha proporcionado la clave API. Defina la variable de entorno 'API_KEY'.")


# Iniciar la aplicación
mostrar_menu()
