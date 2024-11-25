# importamos el módulo random 
import random

def piedra_papel_tijera():
    # damos un mensaje de bienvenida
    print("¡bienvenido al juego de piedra, papel o tijera!")
    
    # creamos una lista con las opciones para jugar
    opciones = ["piedra", "papel", "tijera"]

    # iniciamos un bucle que continua hasta que el jugador decida salir
    while True:
        # solicitamos al jugador que elija entre las opciones o que escriba 'salir'
        jugador = input("elige: piedra, papel o tijera (o escribe 'salir' para terminar): ").lower()
        
        # verificamos si el jugador quiere salir del juego
        if jugador == "salir":
            print("¡gracias por jugar! nos vemos pronto.")
            break  # Salimos del bucle para terminar el juego

        # verificamos si la entrada del jugador es válida (debe estar en la lista de opciones)
        if jugador not in opciones:
            print("opción inválida. por favor, elige piedra, papel o tijera.")
            continue  # volvemos al inicio del bucle para pedir una opción válida

        # la computadora hace su elección al azar de la lista de opciones
        computadora = random.choice(opciones)
        print(f"la computadora eligió: {computadora}")

        # comparamos las elecciones para determinar el resultado
        if jugador == computadora:
            # si ambas elecciones son iguales, es un empate
            print("es un empate.")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            # estas son las condiciones en las que el jugador gana
            print("¡ganaste!")
        else:
            # si no es empate ni el jugador gana, entonces la computadora gana
            print("perdiste.")

# llamamos a la función para iniciar el juego
piedra_papel_tijera()
