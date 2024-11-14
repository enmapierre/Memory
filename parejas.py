import random

# Solicitar el tamaño del tablero al usuario
filas = int(input("Dime el número de filas que quieres que tenga el tablero (entre 2 y 6): "))
columnas = int(input("Dime el número de columnas que quieres que tenga el tablero (entre 2 y 5): "))

# Validar el tamaño del tablero
while filas < 2 or filas > 6 or columnas < 2 or columnas > 5 or (filas * columnas) % 2 != 0:
    print("Tamaño no válido. Las filas deben estar entre 2 y 6 y las columnas entre 2 y 5, y el número total de cartas debe ser par.")
    filas = int(input("Dime el número de filas que quieres que tenga el tablero (entre 2 y 6): "))
    columnas = int(input("Dime el número de columnas que quieres que tenga el tablero (entre 2 y 5): "))

# Variables principales
tablero = []
tablero_oculto = []
total_cartas = filas * columnas
puntos_jugador1 = 0
puntos_jugador2 = 0
turno_jugador1 = True  # Variable que controla el turno del jugador actual

def crear_tablero():
    emoticonos = [
        "😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊",
        "😋", "😎", "😍", "😘", "😗", "😙", "😚", "🙂", "🤗", "🤩",
        "🤔", "🤨", "😐", "😑", "😶", "🙄", "😏", "😣", "😥", "😮",
        "🤐", "😯", "😪", "😫", "🥱", "😴", "😌", "🤤", "😛", "😜",
        "😝", "🤪", "😒", "😓", "😔", "😕", "🙃", "🤑", "😲", "☹️"
    ]

    # Seleccionar emoticonos aleatorios y crear parejas
    num_parejas = total_cartas // 2
    emoticonos_seleccionados = random.sample(emoticonos, num_parejas)
    parejas = emoticonos_seleccionados * 2
    random.shuffle(parejas)  # Mezclar las parejas para aleatoriedad

    # Llenar `tablero` con "#"
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("#")  # Cada posición oculta se representa con "#"
        tablero.append(fila)

    # Llenar `tablero_oculto` con los emoticonos de parejas
    indice = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(parejas[indice])  # Asignar emoticono a la celda correspondiente
            indice += 1
        tablero_oculto.append(fila)

    # Imprimir tablero inicial
    mostrar_tablero(tablero)
    mostrar_tablero(tablero_oculto)


def mostrar_tablero(tablero):
    print("TABLERO:")
    for fila in tablero:
        print(" ".join(fila))


def jugador_vs_jugador():
    global puntos_jugador1, puntos_jugador2, turno_jugador1

    # Iniciar el juego hasta que se encuentren todas las parejas
    while puntos_jugador1 + puntos_jugador2 < total_cartas :
        if turno_jugador1:
            jugador_actual = "Jugador 1"
        else:                                   #jugador_actual = "Jugador 1" if turno_jugador1 else "Jugador 2" es igual que esto
            jugador_actual = "Jugador 2"
        
        print(f"\nComienz el turno del {jugador_actual}")

        # Solicitar primera carta
        print("\nDime las coordenadas de tu primera carta:")
        pos_x1 = int(input(f"Fila (1 a {filas}): ")) - 1
        pos_y1 = int(input(f"columna (1 a {columnas}): ")) - 1

        # Mostrar primera carta en el tablero temporalmente
        tablero[pos_x1][pos_y1] = tablero_oculto[pos_x1][pos_y1]
        mostrar_tablero(tablero)

        # Solicitar segunda carta
        print("\nDime las coordenadas de tu segunda carta:")
        pos_x2 = int(input(f"Fila (1 a {filas}): ")) - 1
        pos_y2 = int(input(f"Columna (1 a {columnas}): ")) - 1

        # Verificar que las posiciones están dentro del rango
        if (pos_x1 < 0 or pos_x1 >= filas or pos_y1 < 0 or pos_y1 >= columnas or
            pos_x2 < 0 or pos_x2 >= filas or pos_y2 < 0 or pos_y2 >= columnas):
            print("Las posiciones están fuera del rango. Por favor, vuelve a introducir las coordenadas.")
            continue

        # Mostrar ambas cartas seleccionadas
        tablero[pos_x2][pos_y2] = tablero_oculto[pos_x2][pos_y2]
        mostrar_tablero(tablero)

        # Verificar si las cartas coinciden
        if tablero_oculto[pos_x1][pos_y1] == tablero_oculto[pos_x2][pos_y2]:
            print(f"¡{jugador_actual} has encontrado una pareja!, continua tu turno")
            if turno_jugador1:
                puntos_jugador1 += 2
            else:
                puntos_jugador2 += 2
        else:
            print(f"oh! no.... has fallado no has encontrado la pareja :(. Turno para el otro jugador.")
            # Restablecer las cartas si no coinciden
            tablero[pos_x1][pos_y1] = "#"
            tablero[pos_x2][pos_y2] = "#"
            turno_jugador1 = not turno_jugador1  # Cambiar de jugador si no acertó
        
        # Mostrar el tablero actualizado
        mostrar_tablero(tablero)

    # Determinar el ganador
    if puntos_jugador1 > puntos_jugador2:
        print("\n¡Jugador 1 gana con {} puntos!".format(puntos_jugador1))
    elif puntos_jugador2 > puntos_jugador1:
        print("\n¡Jugador 2 gana con {} puntos!".format(puntos_jugador2))
    else:
        print("\n¡Es un empate!")


def jugador_vs_maquina():
    global puntos_jugador1, puntos_jugador2, turno_jugador1
    memoria_maquina = {} 

    # Iniciar el juego hasta que se encuentren todas las parejas
    while puntos_jugador1 + puntos_jugador2 < total_cartas:
        if turno_jugador1:
            jugador_actual = "Jugador 1"
        else:                                   #jugador_actual = "Jugador 1" if turno_jugador1 else "Máquina" es igual a esto
            jugador_actual = "Máquina"
        
        print(f"\nComienza el turno de {jugador_actual}")

        if turno_jugador1:
            # Turno del jugador 1
            print("\nDime las coordenadas de tu primera carta:")
            pos_x1 = int(input(f"Fila (1 a {filas}): ")) - 1
            pos_y1 = int(input(f"Columna (1 a {columnas}): ")) - 1

            tablero[pos_x1][pos_y1] = tablero_oculto[pos_x1][pos_y1]
            mostrar_tablero(tablero)
            #Recordar primera carta 
            memoria_maquina[(pos_x1, pos_y1)] = tablero_oculto[pos_x1][pos_y1]

            print("\nDime las coordenadas de tu segunda carta:")
            pos_x2 = int(input(f"Fila (1 a {filas}): ")) - 1
            pos_y2 = int(input(f"Columna (1 a {columnas}): ")) - 1

            if (pos_x1 < 0 or pos_x1 >= filas or pos_y1 < 0 or pos_y1 >= columnas or
                pos_x2 < 0 or pos_x2 >= filas or pos_y2 < 0 or pos_y2 >= columnas):
                print("Las posiciones están fuera del rango. Por favor, vuelve a introducir las coordenadas.")
                continue

            tablero[pos_x2][pos_y2] = tablero_oculto[pos_x2][pos_y2]
            mostrar_tablero(tablero)
            #Recordar segunda carta 
            memoria_maquina[(pos_x2, pos_y2)] = tablero_oculto[pos_x2][pos_y2]

            if tablero_oculto[pos_x1][pos_y1] == tablero_oculto[pos_x2][pos_y2]:
                print("¡Jugador 1 has encontrado una pareja! Continúa tu turno.")
                puntos_jugador1 += 2
                # Eliminar las cartas emparejadas de la memoria
                memoria_maquina.pop((pos_x1, pos_y1), None)
                memoria_maquina.pop((pos_x2, pos_y2), None)
            else:
                print("Oh! no.... no has encontrado la pareja. Turno para la máquina.")
                tablero[pos_x1][pos_y1] = "#"
                tablero[pos_x2][pos_y2] = "#"
                turno_jugador1 = not turno_jugador1

        else:
             # Turno de la máquina
            pareja_encontrada = False
            pos_x1, pos_y1 = None, None
            pos_x2, pos_y2 = None, None
            # La máquina intenta encontrar una pareja con las cartas en memoria
             # La máquina intenta encontrar una pareja en su memoria
            for (x1, y1), valor1 in memoria_maquina.items():
                for (x2, y2), valor2 in memoria_maquina.items():
                    if (x1, y1) != (x2, y2) and valor1 == valor2:
                        pos_x1, pos_y1 = x1, y1
                        pos_x2, pos_y2 = x2, y2
                        pareja_encontrada = True
                        break
                if pareja_encontrada:
                    break
                
                
            if pareja_encontrada:
                print(f"La máquina ha encontrado una pareja en ({pos_x1 + 1}, {pos_y1 + 1}) y ({pos_x2 + 1}, {pos_y2 + 1})")
                tablero[pos_x1][pos_y1] = tablero_oculto[pos_x1][pos_y1]
                tablero[pos_x2][pos_y2] = tablero_oculto[pos_x2][pos_y2]
                mostrar_tablero(tablero)
                puntos_jugador2 += 2
                # Eliminar las cartas emparejadas de la memoria
                memoria_maquina.pop((pos_x1, pos_y1), None)
                memoria_maquina.pop((pos_x2, pos_y2), None)

            else:
                # Seleccionar primera carta aleatoria si no hay parejas conocidas
                opciones = []
                for i in range(filas):
                    for j in range(columnas):
                        if tablero[i][j] == "#":
                            opciones.append((i, j))
                pos_x1, pos_y1 = random.choice(opciones)
                tablero[pos_x1][pos_y1] = tablero_oculto[pos_x1][pos_y1]
                print(f"La máquina ha seleccionado la posición ({pos_x1 + 1}, {pos_y1 + 1})")
                mostrar_tablero(tablero)
                # Memorizar la carta desvelada
                memoria_maquina[(pos_x1, pos_y1)] = tablero_oculto[pos_x1][pos_y1]

                # Verificar si la primera carta desvelada tiene pareja en la memoria
                pareja_encontrada = False
                for (x, y), valor in memoria_maquina.items():
                    if (x, y) != (pos_x1, pos_y1) and valor == tablero_oculto[pos_x1][pos_y1]:
                        pos_x2, pos_y2 = x, y
                        pareja_encontrada = True
                        break

                if pareja_encontrada:
                    print(f"La máquina ha encontrado la pareja de la carta en ({pos_x1 + 1}, {pos_y1 + 1}) en ({pos_x2 + 1}, {pos_y2 + 1})")
                    tablero[pos_x2][pos_y2] = tablero_oculto[pos_x2][pos_y2]
                    mostrar_tablero(tablero)
                    puntos_jugador2 += 2
                    # Eliminar las cartas emparejadas de la memoria
                    memoria_maquina.pop((pos_x1, pos_y1), None)
                    memoria_maquina.pop((pos_x2, pos_y2), None)
                else:
                    # Seleccionar segunda carta aleatoria si no encontró pareja
                    opciones_filtradas = []
                    for (i, j) in opciones:
                        if (i, j) != (pos_x1, pos_y1):
                            opciones_filtradas.append((i, j))
                    pos_x2, pos_y2 = random.choice(opciones_filtradas)
                    tablero[pos_x2][pos_y2] = tablero_oculto[pos_x2][pos_y2]
                    print(f"La máquina ha seleccionado la posición ({pos_x2 + 1}, {pos_y2 + 1})")
                    mostrar_tablero(tablero)
                    # Memorizar la segunda carta desvelada
                    memoria_maquina[(pos_x2, pos_y2)] = tablero_oculto[pos_x2][pos_y2]

                    # Verificar si las cartas coinciden
                    if tablero_oculto[pos_x1][pos_y1] == tablero_oculto[pos_x2][pos_y2]:
                        print("¡La máquina ha encontrado una pareja!")
                        puntos_jugador2 += 2
                        # Eliminar las cartas emparejadas de la memoria
                        memoria_maquina.pop((pos_x1, pos_y1), None)
                        memoria_maquina.pop((pos_x2, pos_y2), None)
                    else:
                        print("La máquina no ha encontrado la pareja.")
                        tablero[pos_x1][pos_y1] = "#"
                        tablero[pos_x2][pos_y2] = "#"
                        turno_jugador1 = True

        # Mostrar el tablero actualizado
        mostrar_tablero(tablero)

    # Determinar el ganador
    if puntos_jugador1 > puntos_jugador2:
        print("\n¡Jugador 1 gana con {} puntos!".format(puntos_jugador1))
    elif puntos_jugador2 > puntos_jugador1:
        print("\n¡La máquina gana con {} puntos!".format(puntos_jugador2))
    else:
        print("\n¡Es un empate!")


# Menú principal
def menu():
    while True:
        print("\n1. Iniciar juego (Jugador vs Jugador)")
        print("2. Iniciar juego (Jugador vs Máquina)")
        print("3. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            crear_tablero()
            jugador_vs_jugador()
        elif opcion == 2:
            crear_tablero()
            jugador_vs_maquina()
        elif opcion == 3:
            print("Saliendo del juego...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 3.")

# Iniciar el menú
menu()
