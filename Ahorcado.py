import random  

palabras=["python", "programacion", "sistemas", "compilador", "circuito", "computadora", "estructura", "datos"]   

ahorcado_dibujo=[
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
]

def mostrar_estado (vidas, letras_adivinadas, letras_incorrectas):  # función para mostrar el estado del juego

    print (ahorcado_dibujo[6-vidas])

    print ("Palabra: ", end="")
    for letra in letras_adivinadas:   # imprimo las letras adivinadas
        print(letra, end=" ")
    print()

    print("Letras incorrectas: ", end="")
    for letra in letras_incorrectas:        # imprimo las letras incorrectas
        print(letra, end=" ")
    print()

    print(f"Vidas restantes: {vidas}")    # las vidas del jugador

palabra_secreta=random.choice(palabras)
letras_adivinadas=["_"]*len(palabra_secreta)    # para el funcionamiento del juego
letras_incorrectas=[]
vidas=6
ganado=False

print ("¡Bienvenido al juego del AHORCADO!")

while vidas>0 and ganado==False:

    mostrar_estado(vidas, letras_adivinadas, letras_incorrectas)    # muestro el estado del juego mediante la llamada a la función

    valido=True
    while valido:
        try:
            letra=input("Ingrese una letra: ").lower()
            if not letra.isalpha() or len(letra)!=1:
                raise ValueError ("Debes ingresar una sola letra válida.")      # control para el ingreso del usuario
            valido=False
        except ValueError as e:
            print (e)

    if letra in letras_adivinadas or letra in letras_incorrectas:   # controlo que no ingrese letras repetidas
        print (f"Ya intentaste con la letra {letra}, probá con otra.")
    else:
        if letra in palabra_secreta:
            for i in range (len(palabra_secreta)):   # si la letra no es repetida, la reemplazo en las letras adivinadas
                if palabra_secreta[i]==letra:
                    letras_adivinadas[i]=letra
        else:
            letras_incorrectas.append(letra)     # sino, la agrego a la lista de letras incorrectas
            vidas-=1  # resto una vida, lo que luego va a afectar al dibujito del ahorcado

    if "_" not in letras_adivinadas:   # si no hay más guiones en las letras adivinadas, signifca que el jugador ya ganó
        ganado=True

if ganado:
    print (f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")      # mensajes de salida en cada caso
else:
    print (ahorcado_dibujo[6])
    print (f"Te quedaste sin vidas. La palabra era: {palabra_secreta}")
