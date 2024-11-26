import random
import string
tamaño=15
palabras=['ZAFIRO', 'ESPIRITU', 'INSTITUTO', 'METALURGICA', 'CUADERNO']
matriz=None

def generar_matriz(tamaño):
    return [[' ' for _ in range(tamaño)] for _ in range(tamaño)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))

def colocar_palabra(matriz, palabra, dirección, fila, columna):
    if dirección == 'H':
        for i, letra in enumerate(palabra):
            matriz[fila][columna + i] = letra
    elif dirección == 'V':
        for i, letra in enumerate(palabra):
            matriz[fila + i][columna] = letra

def verificar_posición(matriz, palabra, dirección, fila, columna):
    if dirección == 'H' and columna + len(palabra) > len(matriz):
        return False
    elif dirección == 'V' and fila + len(palabra) > len(matriz):
        return False
    for i, letra in enumerate(palabra):
        if dirección == 'H' and matriz[fila][columna + i] != ' ':
            return False
        elif dirección == 'V' and matriz[fila + i][columna] != ' ':
            return False
    return True

def insertar_palabras(matriz, palabras):
    for palabra in palabras:
        colocada = False
        intentos = 0
        while not colocada and intentos < 100:
            dirección = random.choice(['H', 'V'])
            if dirección == 'H':
                fila = random.randint(0, len(matriz) - 1)
                columna = random.randint(0, len(matriz) - len(palabra))
            elif dirección == 'V':
                fila = random.randint(0, len(matriz) - len(palabra))
                columna = random.randint(0, len(matriz) - 1)
            if verificar_posición(matriz, palabra, dirección, fila, columna):
                colocar_palabra(matriz, palabra, dirección, fila, columna)
                colocada = True
            intentos += 1
        if not colocada:
            print(f"No se pudo colocar la palabra: {palabra}")

def rellenar_matriz(matriz):
    letras = string.ascii_uppercase
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == ' ':
                matriz[fila][columna] = random.choice(letras)

def verificar_palabra(palabra, fila, columna, dirección):
    if palabra not in palabras:
        return False
    temp_matriz = generar_matriz(tamaño)
    colocar_palabra(temp_matriz, palabra, dirección, fila, columna)
    for i in range(tamaño):
        for j in range(tamaño):
            if temp_matriz[i][j] != ' ' and temp_matriz[i][j] != matriz[i][j]:
                return False
    return True
palabras_acertadas=0
def jugar():
    global matriz
    matriz = generar_matriz(tamaño)
    insertar_palabras(matriz, palabras)
    rellenar_matriz(matriz)
    imprimir_matriz(matriz)
    global palabras_acertadas
    while palabras_acertadas<5:
        opcion= input("Ingresa la palabra, fila, columna y dirección (ejemplo: MONO 1 2 H) o 'salir' para terminar: ")
        if opcion.lower() == 'salir':
            break
        palabra, fila, columna, dirección = opcion.split()
        fila = int(fila)
        columna = int(columna)
        
        if verificar_palabra(palabra, fila, columna, dirección):
            print(f"¡Correcto!, {palabra} esta en la sopa de letras.")
            palabras_acertadas+=1
        else:
            print(f"Incorrecto, {palabra} no está en esas coordenadas. Inténtalo de nuevo.")
        imprimir_matriz(matriz)
    if palabras_acertadas==len(palabras):
        print(f"¡Felicitaciones!, encontraste todas las palabras.")
    else:
        print(f"Encontraste {palabras_acertadas} palabras de cinco, intentalo de nuevo.\n¡Buena suerte!")
jugar()
