from obtenerClima import obtener_clima
from menu import mostrar_menu

def cambiar_datos():
    
    while True:
        unidad = input ("Ingrese que unidad desea Celcius ('C') o Fahrenheit ('F'): ")

        if unidad.upper() == "C":
            unidadMedida = "metric"
            obtener_clima(unidadMedida)
            break
        elif unidad.upper() == "F":
            unidadMedida = "imperial"
            obtener_clima(unidadMedida)
            break
        else: 
            print("Caracter incorrecto. Vuelva a intentarlo: ")


mostrar_menu()