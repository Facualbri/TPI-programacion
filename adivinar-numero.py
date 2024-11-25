import random

matriz = []
for i in range(3):
    matriz.append([0] * 3)

numero_secreto = random.randint(1, 15)

intentos_restantes = 9
ganador = False

while ganador == False and intentos_restantes > 0:
    for fila in matriz:
        for celda in fila:
            print("|", celda, end=" | ")
        print("\n-----------------")

    adivinanza = int(input("Adivina el número (1-15): "))

    if adivinanza == numero_secreto:
        print("ADIVINASTE")
        ganador = True
    else:
        print("Número incorrecto. Intenta de nuevo.")
        intentos_restantes -= 1

        fila = (9 - intentos_restantes - 1) // 3
        columna = (9 - intentos_restantes - 1) % 3
        matriz[fila][columna] = adivinanza

if ganador == False:
    print(f"Te quedaste sin intentos y el número era {numero_secreto}.")