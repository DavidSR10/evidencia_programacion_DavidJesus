"""
Diseña una aplicación que pida por consola una ciudad de destino. Si introduces un 0 y
pulsas intro, sales de la aplicación. (5 puntos).
● Si introduces madrid, sevilla o valencia, te permite continuar y te pregunta cuántas
noches de hotel necesitas. Es indiferente que escribas las ciudades en mayúsculas o
minúsculas.. (5 puntos)
● Al escribir las noches de hotel te muestra un error si no introduces un número. (5
puntos)
● Una vez finalizado, te muestra un mensaje indicando la ciudad y las noches de hotel
que has introducido. Todas (5 puntos)
● Razona qué tipo de estructura utilizas y por qué. Explicación de código y manejo de
errores. (5 puntos)
"""
def solicitar_ciudad():
    while True:
        ciudad_destino = input("Ingrese una ciudad de destino Madrid, Sevilla o Valencia, (ingrese 0 para salir): ").lower()

        if ciudad_destino == "0":
            print("Saliendo de la aplicación.")
            return None
        elif ciudad_destino in {"madrid", "sevilla", "valencia"}:
            return ciudad_destino
        else:
            print("Ciudad no válida. Por favor, elige entre Madrid, Sevilla o Valencia.")

def solicitar_noches(ciudad):
    while True:
        try:
            noches_hotel = int(input(f"¿Cuántas noches de hotel necesitas en {ciudad.capitalize()}? "))
            return noches_hotel
        except ValueError:
            print("Por favor, ingresa un número válido para las noches de hotel.")

def main():
    ciudad = solicitar_ciudad()

    if ciudad is not None:
        noches_hotel = solicitar_noches(ciudad)
        print(f"Has seleccionado {ciudad.capitalize()} como destino y necesitas {noches_hotel} {'noche' if noches_hotel == 1 else 'noches'} de hotel.")

if __name__ == "__main__":
    main()
