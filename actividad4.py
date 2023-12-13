"""
Inicia la aplicación y genera un número aleatorio entre el 1 y el 9 (5 puntos) ∙ La
aplicación nos pide que adivinemos este número aleatorio. Seguirá mostrando el
mensaje hasta que hayamos adivinado el número (5 puntos)
● Muestra el total de intentos que has necesitado para adivinar el número. Si has
necesitado más de 3 muestra un mensaje indicando que prueba no superada (5
puntos)
● No puedes repetir un número que ya hayas indicado (5 puntos)
● Muestra cuánto tiempo tarda el programa en ejecutarse desde su inicio hasta que
muestra el mensaje final que el número ha sido adivinado (5 puntos)
"""
import random
import time

# Códigos ANSI para cambiar el color de la salida en la consola
COLOR_AMARILLO = "\033[93m"
COLOR_AZUL = "\033[94m"
COLOR_ROJO = "\033[91m"
COLOR_RESET = "\033[0m"


def juego_adivinanza():
    # Generar un número aleatorio entre 1 y 9
    numero_secreto = random.randint(1, 9)

    print("¡Bienvenido al juego de adivinanza!")
    print("Intenta adivinar el número secreto entre 1 y 9.")

    intentos = 0
    numeros_adivinados = set()
    inicio_tiempo = time.time()

    while True:
        # Pedir al usuario que ingrese un número
        intento = input("Ingresa un número: ")

        # Validar si el input es un número
        if not intento.isdigit():
            print("Por favor, ingresa un número válido.")
            continue

        # Convertir el input a entero
        intento = int(intento)

        # Validar si el número ya fue ingresado
        if intento in numeros_adivinados:
            print("Ya has ingresado ese número. Prueba con otro.")
            continue

        # Incrementar el contador de intentos
        intentos += 1

        # Añadir el número a los números adivinados
        numeros_adivinados.add(intento)

        # Verificar si el número es el correcto
        if intento == numero_secreto:
            fin_tiempo = time.time()
            tiempo_transcurrido = fin_tiempo - inicio_tiempo
            print(f"{COLOR_AZUL}¡Felicidades! ¡Has adivinado el número en {intentos} intentos!{COLOR_RESET}")
            print(f"{COLOR_AMARILLO}Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos.{COLOR_RESET}")

            if intentos > 3:
                print(f"{COLOR_ROJO}Prueba no superada. Has necesitado más de 3 intentos.{COLOR_RESET}")
            break
        else:
            print("Número incorrecto. Sigue intentando.")


if __name__ == "__main__":
    juego_adivinanza()

