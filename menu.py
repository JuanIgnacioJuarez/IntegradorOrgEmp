from obtenerClima import obtener_clima
from cambiarDatos import cambiar_datos

def mostrar_menu():
    while True:
        print ("Ingrese la opción que desea realizar: ")
        print ("--------------------------------")
        print ("1- Consultar clima: ")
        print ("2- Cambiar unidades: ")
        print ("Salir")
        opcion = input()

        if opcion == "1":
            obtener_clima()
        elif opcion == "2":
            cambiar_datos()
        elif opcion.lower == "salir":
            break
        else:
            print("Opción incorrecta, vuelva a intentarlo.")