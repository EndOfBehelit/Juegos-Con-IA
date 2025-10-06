import random

#Tamaño del tablero
FILAS = 3
COLUMNAS = 3
GANA = 3

#Pintar el tablero
tablero = []
for _ in range(FILAS):  
    fila = [' ' for _ in range(COLUMNAS)] 
    tablero.append(fila)

#Imprimir el tablero
def imprimir_tablero():
    print(f"  0    1    2")
    for contador, i in enumerate(tablero):
        print(f"{i} -> {contador}")

#Comprobar si el tablero está lleno
def tablero_lleno():
    full = True
    for fila in tablero:
        for casilla in fila:
            if casilla == ' ':
                full = False
                break
    return full

#Comprobar si un jugador ha ganado
def verificar_ganador():
    '''1 para gana la IA, -1 para gana el jugador, 0 para empate, 
    None para seguir jugando'''
    win_player = ['X', 'X', 'X']
    win_IA = ['O', 'O', 'O']

    win = None

    for fila in tablero: #COMPROBAR 4 SEGUIDAS EN HORIZONTAL
        if win_player == fila:
            win = -1
            return win
        if win_IA == fila:
            win = 1
            return win     
    
    transpuesta = [[fila[i] for fila in tablero] for i in range(COLUMNAS)] #CAMBIO FILAS POR COLUMNAS
    for fila in transpuesta: #COMPROBAR 4 SEGUIDAS EN VERTICAL
        if win_player == fila:
            win = -1
            return win
        if win_IA == fila:
            win = 1
            return win 
        
    #COMRPOABR DIOAGONAL DESCENDENTE
    diag_desc = [tablero[i][i] for i in range(len(tablero))]
    if win_player == diag_desc:
        win = -1
        return win
    if win_IA == diag_desc:
        win = 1
        return win
    
    #COMPROBAR DIAGONAL HACIA LA IZQUIERDA
    diag_asc = [tablero[i][len(tablero) - 1 - i] for i in range(len(tablero))]
    if win_player == diag_asc:
        win = -1
        return win
    if win_IA == diag_asc:
        win = 1
        return win
    #COMPROBAR EMPATE
    if tablero_lleno():
        win = 0
        return win
            
    return win

def colocarFichaJugador(x, y):
    if x > 2 or y > 2 or x < 0 or y < 0:
        return False
    if tablero[x][y] == ' ':
        tablero[x][y] = 'X'
        return True
    else:
        return False

def colocarFichaIARandom():
    while True:
        r1 = random.randint(0, len(tablero)-1)
        r2 = random.randint(0, len(tablero)-1)

        if tablero[r1][r2] == ' ':
            tablero[r1][r2] = 'O'
            return True

def colocarFichaIACalculada():
    pos_vacias = posVacias(tablero)
    mejor_puntuacion = -5
    mejor_movimiento = (-1,-1)

    for i in pos_vacias:
        tablero[i[0]][i[1]] = 'O'
        jugador = True
        #puntuacion, _ = minimax(tablero, jugador) he visto que esto también sirve pero me aclaro mejor con lo otro
        puntuacion = minimax(tablero, jugador) #Ahora devuelve tupla, por lo que sólo me interesa la posición 0.
        tablero[i[0]][i[1]] = ' '

        if puntuacion[0] > mejor_puntuacion:
            mejor_puntuacion = puntuacion[0]
            mejor_movimiento = i

    if tablero[mejor_movimiento[0]][mejor_movimiento[1]] == ' ':
        tablero[mejor_movimiento[0]][mejor_movimiento[1]] = 'O'

    return None

#Minimax
def minimax(tablero, jugador, profundidad=0):
    '''Ahora devuelve una tupla con (puntuacion, profundidad).'''
    puntuacion = verificar_ganador()
    if puntuacion is not None:
        return (puntuacion, profundidad)

    pos_vacias = posVacias(tablero)

    if jugador:
        mejor_puntuacion = (5,10) #tupla con (puntuacion, profundidad)
        for i in pos_vacias:
            tablero[i[0]][i[1]] = 'X'
            jugador = False
            puntuacion = minimax(tablero, jugador, profundidad + 1)
            tablero[i[0]][i[1]] = ' '
            if (mejor_puntuacion[0] == puntuacion[0]):
                mejor_puntuacion = (mejor_puntuacion[0], min(mejor_puntuacion[1], puntuacion[1])) #En caso de tener misma puntuacion, premia la profundidad más baja
            elif(mejor_puntuacion[0] > puntuacion[0]):
                mejor_puntuacion = puntuacion
            else:
                continue
        return mejor_puntuacion
    else:
        mejor_puntuacion = (-5, 10)
        for i in pos_vacias:
            tablero[i[0]][i[1]] = 'O'
            jugador = True
            puntuacion = minimax(tablero, jugador, profundidad + 1)
            tablero[i[0]][i[1]] = ' '
            if (mejor_puntuacion[0] == puntuacion[0]):
                mejor_puntuacion = (mejor_puntuacion[0], min(mejor_puntuacion[1], puntuacion[1])) #En caso de tener misma puntuacion, premia la profundidad más baja
            elif(mejor_puntuacion[0] < puntuacion[0]):
                mejor_puntuacion = puntuacion
            else:
                continue
        return mejor_puntuacion

def posVacias(tablero):
    pos_libres = []
    for fila in range(len(tablero)):
        for col in range(len(tablero[0])):
            if tablero[fila][col] == " ":
                pos_libres.append((fila, col))   

    return pos_libres

#Bucle del juego
def jugar():
    jugador = 'X'
    jugador_ia = 'O'
    while not tablero_lleno() or verificar_ganador() is not None:
        print("Turno del jugador: ")
        x = int(input("Coordenada x (fila): "))
        y = int(input("Coordenada y (columna): "))
        while not colocarFichaJugador(x, y):
            print("Prueba otra vez: ")
            x = int(input("Coordenada x (fila): "))
            y = int(input("Coordenada y (columna): "))
        if verificar_ganador() == -1: #Al colocar el jugador, puede ganar o empatar o seguir jugando
            print("Has ganado")
            break
        if tablero_lleno():
            print("Se ha llenado el tablero")
            print("EMPATE")
            break

        print("Turno de la máquina: ")

        #colocarFichaIARandom()
        colocarFichaIACalculada()

        if verificar_ganador() == 1:#Al colocar la IA, puede ganar o empatar o seguir jugando
            print("Ha ganado la IA")
            break
        if tablero_lleno():
            print("Se ha llenado el tablero")
            break
        imprimir_tablero()


#Ejecutar el juego
imprimir_tablero()
jugar()
imprimir_tablero()
print("FIN DEL JUEGO")
