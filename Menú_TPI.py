def juego_maga():
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
        |    |
        O    |
       /|\   |
       /     |
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
    
def juego_facu():
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

def juego_santino():
    import random
    import time
    print("¡Bienvenido a la mesa de blackjack! \nRepasemos brevemente las reglas del juego:",end="\n")
    print("*El jugador compite contra el crupier\n*El valor de las cartas es el siguiente: las cartas del 2 al 10 valen su numero,\nlas figuras J, Q, K (en este juego representadas por '10') valen 10\ny los ases (en este juego representados por '11') pueden valer 1 u 11.\n*El jugador que tenga blackjack (dos cartas que sumen 21) o la puntuacion mas alta sin pasarse de 21 gana.\n*Si el jugador y el crupier tienen la misma puntuacion, se produce un empate y el jugador recupera su apuesta.\n*El crupier se planta en 17.\n*El jugador puede plantarse o pedir mas cartas hasta alcanzar los 21 puntos.\n",end="\n")
    time.sleep(10)
    #Inicio las variables para los ciclos
    i=0
    a=0
    b=0
    c=0
    f=0
    g=0
    h=0

    saldo=1000
    jugador=input("Ingrese su nombre de jugador: ")
    time.sleep(1)
    while i==0:
        #ciclo apuesta
        while a==0:
            print(f"Este es tu saldo: ${saldo}")
            time.sleep(1)
            apuesta=int(input("¿Cuanto desea apostar?: "))
            if saldo >= apuesta and apuesta >= 0:
                saldo = saldo-apuesta
                a = 1
            elif saldo < apuesta:
                print("¡Saldo insuficiente!")
                time.sleep(1)
        time.sleep(1)
        a = 0

        #Cartas y tirada
        cartas_jugador=[]
        cartas=[2,3,4,5,6,7,8,9,10,10,10,10,11]
        cartasC=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
        random1= random.randint(0,12)
        random2= random.randint(0,12)
        primera_carta = cartas[random1]
        segunda_carta = cartas[random2]
        total = primera_carta + segunda_carta
        print("*Barajando el mazo*")
        time.sleep(2)
        print("Su primera carta es:")
        time.sleep(1)
        print(primera_carta)
        time.sleep(2)
        print("Su segunda carta es:")
        time.sleep(1)
        print(segunda_carta)
        time.sleep(1)
        
        #si obtiene un As o no
        if not primera_carta == 11 and not segunda_carta == 11:
            cartas_jugador.append(primera_carta)
            cartas_jugador.append(segunda_carta)
            total = primera_carta + segunda_carta
            print(f"La suma de tus cartas es: {total}")
        if primera_carta == 11:
                    while f==0:
                        print(f"Tienes un As, posibles valores: {segunda_carta+1}(1) o {segunda_carta+11}(11)")
                        valor_as = int(input("Ingrese su decision (1 o 11): "))
                        if valor_as == 1:
                            primera_carta = 1
                            cartas_jugador.append(primera_carta)
                            total_jugador = sum(cartas_jugador)
                            f = 1
                        elif valor_as == 11:
                            primera_carta = 11
                            cartas_jugador.append(primera_carta)
                            total_jugador = sum(cartas_jugador)
                            f = 1
                        else:
                            print("Error: ¡Ingrese un numero valido!")
                    time.sleep(1)
                    f = 0
                    print(f"La suma de tus cartas es: {total_jugador}")
        if segunda_carta == 11:
                    while g==0:
                        print(f"Tienes un As, posibles valores: {primera_carta+1}(1) o {primera_carta+11}(11)")
                        valor_as = int(input("Ingrese su decision (1 o 11): "))
                        if valor_as == 1:
                            segunda_carta = 1
                            cartas_jugador.append(segunda_carta)
                            total_jugador = sum(cartas_jugador)
                            g = 1
                        elif valor_as == 11:
                            segunda_carta = 11
                            cartas_jugador.append(segunda_carta)
                            total_jugador = sum(cartas_jugador)
                            g = 1
                        else:
                            print("Error: ¡Ingrese un numero valido!")
                    time.sleep(1)
                    g = 0
                    print(f"La suma de tus cartas es: {total_jugador}")
                    
        
        time.sleep(2)
        random_crupier = random.randint(0,13)
        crupier_carta1  = cartasC[random_crupier]
        print(f"El crupier obtuvo un: {crupier_carta1}")
        time.sleep(2)
        
        #si el jugador pide mas cartas
        total_jugador = sum(cartas_jugador)
        while b==0 and total_jugador<=21:
            otra_carta = input("Escribe 'Pido' si quieres otra carta o 'Planto' si te quieres quedar: ")
            otra_carta = otra_carta.upper()
            if otra_carta == "PIDO":
                random3 = random.randint(0,12)
                carta_pedida = cartas[random3]
                time.sleep(1)
                print(f"Obtuviste un: {carta_pedida}")
                time.sleep(1)
                if carta_pedida == 11:
                    while c==0:
                        valor_as = int(input("Tienes un As, elije su valor (1 o 11): "))
                        if valor_as == 1:
                            carta_pedida = 1
                            cartas_jugador.append(carta_pedida)
                            total_jugador = sum(cartas_jugador)
                            c = 1
                        elif valor_as == 11:
                            carta_pedida = 11
                            cartas_jugador.append(carta_pedida)
                            total_jugador = sum(cartas_jugador)
                            c = 1
                        else:
                            print("Error: ¡Ingrese un numero valido!")
                    time.sleep(1)
                    c = 0
                cartas_jugador.append(carta_pedida)
                total_jugador = sum(cartas_jugador)
                print(f"La suma de tus cartas es: {total_jugador}")
                time.sleep(1)

            if otra_carta == "PLANTO":
                b = 1
        b = 0

        total_jugador = sum(cartas_jugador)
        time.sleep(1)
        print(f"Estas son tus cartas: {cartas_jugador}")
        time.sleep(1)
        print(f"Tu valor total es: {total_jugador} ")
        time.sleep(2)

        #crupier juega
        print("¡Ahora es turno del crupier!")
        time.sleep(2)
        print(f"La primera carta del crupier es: {crupier_carta1}")
        random_crupier2 = random.randint(0,13)
        crupier_carta2 = cartasC[random_crupier2]
        time.sleep(2)
        print(f"El crupier obtiene su segunda carta: {crupier_carta2}")
        cartas_crupier=[]
        cartas_crupier.append(crupier_carta1)
        cartas_crupier.append(crupier_carta2)
        total_crupier = crupier_carta1 + crupier_carta2
        time.sleep(2)
        #si el crupier tiene 16 o menos tiene q arrastrar otra carta
        while h==0 and total_crupier <= 16:
            random4 = random.randint(0,12)
            crupier_arrastrada = cartas[random4]
            time.sleep(2)
            print(f"El crupier arrastro un: {crupier_arrastrada}")
            cartas_crupier.append(crupier_arrastrada)
            total_crupier = sum(cartas_crupier)
            if total_crupier>=21:
                h = 1
        h = 0
        time.sleep(2)
        print(f"La mano del crupier es de {total_crupier} y la suya es de {total_jugador} ")
        time.sleep(2)

        #filtrar el ganador
        if total_jugador == total_crupier and  total_jugador < 21 and total_crupier < 21:
            print("¡Empate!")
            ganancia = apuesta
            saldo += ganancia
        elif total_crupier > 21 and total_jugador > 21:
            print("¡Empate!")
            ganancia = apuesta
            saldo += ganancia
        elif total_jugador <= total_crupier <=21:
            print("¡Crupier gana!")
        elif total_crupier < total_jugador <=21:
            print(f"¡{jugador} gana!")
            ganancia = apuesta*2
            saldo += ganancia
            print(f"${ganancia}")
        elif total_jugador <=21 <total_crupier:
            print(f"¡{jugador} gana!")
            ganancia = apuesta*2
            saldo += ganancia
            print(f"${ganancia}")
        else:
            print("¡Crupier gana!")
        time.sleep(2)

        if saldo==0:
            print("¡Te quedaste sin saldo!")
            i=1
salir=False 
while salir==False:     
    print("***************************************************")
    print("                   Menú de juegos                  ")
    print("***************************************************")
    print("1) Ahorcado\n2) BlackJack\n3) Sopa de letras\n4) Adivina el número\n5) piedra, pepel o tijera\n0) Salir")
    opcion=int(input("Ingrese su opción de juego: "))

    if opcion==0:
        print ("Gracias por jugar...")
        salir=True
    else:
        jugar=True

        if opcion==1:
            while jugar:
                print ("Magalí Pérez")
                juego_maga()
                salir_del_juego=int(input("Ingrese 8 para volver al menú o 9 para volver a jugar: "))
                print()
                if salir_del_juego==8:
                    jugar=False
                elif salir_del_juego==9:
                    jugar=True

        if opcion==2:
            while jugar:
                print ("Santino Volmaro")
                juego_santino()
                salir_del_juego=int(input("Ingrese 8 para volver al menú o 9 para volver a jugar: "))
                if salir_del_juego==8:
                    jugar=False
                elif salir_del_juego==9:
                    jugar=True

        if opcion==3:
            while jugar:
                print ("Mariano Achilli")
                salir_del_juego=int(input("Ingrese 8 para volver al menú o 9 para volver a jugar: "))
                if salir_del_juego==8:
                    jugar=False
                elif salir_del_juego==9:
                    jugar=True

        if opcion==4:
            while jugar:
                print ("Facundo Albri")
                juego_facu()
                salir_del_juego=int(input("Ingrese 8 para volver al menú o 9 para volver a jugar: "))
                if salir_del_juego==8:
                    jugar=False
                elif salir_del_juego==9:
                    jugar=True

        if opcion==5:
            while jugar:
                print ("Bautista Martini")
                salir_del_juego=int(input("Ingrese 8 para volver al menú o 9 para volver a jugar: "))
                if salir_del_juego==8:
                    jugar=False
                elif salir_del_juego==9:
                    jugar=True    