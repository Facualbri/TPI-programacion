salir=False 
while salir==False:     
    print("****************************************************")
    print("                   Menú de juegos                   ")
    print("****************************************************")
    print("1) Ahorcado\n2) BlackJack\n3) Piedra, papel o tijera\n4) Sopa de letras\n5) Juego del Bautista\n0) Salir")
    opcion=int(input("Ingrese su opción de juego: "))

    if opcion==0:
        print ("Gracias por jugar...")
        salir=True
    else:
        jugar=True

        if opcion==1:
            while jugar:
                print ("Magalí Pérez")
                salir_del_juego=int(input("Ingrese 8 para volver al menú o 9 para volver a jugar: "))
                print()
                if salir_del_juego==8:
                    jugar=False
                elif salir_del_juego==9:
                    jugar=True

        if opcion==2:
            while jugar:
                print ("Santino Volmaro")
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