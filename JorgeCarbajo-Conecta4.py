import math

#Tamaño del tablero
FILAS = 6
COLUMNAS = 7
GANA = 4

tablero = [[' ' for col in range(COLUMNAS)] for fila in range(FILAS)]

def imprimir_tablero():
    for fila in tablero:
        print('|' + '|'.join(fila) + '|')
    print('-' * (2 * COLUMNAS + 1))

def tablero_lleno(estado):
    return all(cell != ' ' for fila in estado for cell in fila)

def verificar_ganador_estado(estado, jugador):
    # Horizontal
    for fila in range(FILAS):
        for col in range(COLUMNAS - GANA + 1):
            if all(estado[fila][col + i] == jugador for i in range(GANA)):
                return True
    # Vertical
    for fila in range(FILAS - GANA + 1):
        for col in range(COLUMNAS):
            if all(estado[fila + i][col] == jugador for i in range(GANA)):
                return True
    # Diagonal derecha
    for fila in range(FILAS - GANA + 1):
        for col in range(COLUMNAS - GANA + 1):
            if all(estado[fila + i][col + i] == jugador for i in range(GANA)):
                return True
    # Diagonal izqueirda
    for fila in range(FILAS - GANA + 1):
        for col in range(GANA - 1, COLUMNAS):
            if all(estado[fila + i][col - i] == jugador for i in range(GANA)):
                return True
    return False

def obtener_fila(estado, columna):
    for fila in range(FILAS - 1, -1, -1):
        if estado[fila][columna] == ' ':
            return fila
    return -1

def mov_validos(estado):
    return [col for col in range(COLUMNAS) if estado[0][col] == ' ']

def evaluar_tablero(estado):
    if verificar_ganador_estado(estado, 'O'):
        return 100
    elif verificar_ganador_estado(estado, 'X'):
        return -100
    else:
        return 0

def minimax(estado, profundidad, alpha, beta, maximizing):
    movimientos = mov_validos(estado)
    fin = verificar_ganador_estado(estado, 'O') or verificar_ganador_estado(estado, 'X') or len(movimientos) == 0
    if profundidad == 0 or fin: 
        return evaluar_tablero(estado), None
    if maximizing:
        valor = -math.inf
        mejor_mov = movimientos[0]
        for columna in movimientos:
            fila_disponible = obtener_fila(estado, columna)
            nuevo_estado = [fila[:] for fila in estado]
            nuevo_estado[fila_disponible][columna] = 'O'
            score, _ = minimax(nuevo_estado, profundidad - 1, alpha, beta, False)
            if score > valor:
                valor, mejor_mov = score, columna
            alpha = max(alpha, valor)
            if alpha >= beta: #Elimino rama que sobra
                break
        return valor, mejor_mov
    else:
        valor = math.inf
        mejor_mov = movimientos[0]
        for columna in movimientos:
            fila_disponible = obtener_fila(estado, columna)
            nuevo_estado = [fila[:] for fila in estado]
            nuevo_estado[fila_disponible][columna] = 'X'
            score, _ = minimax(nuevo_estado, profundidad - 1, alpha, beta, True)
            if score < valor:
                valor, mejor_mov = score, columna
            beta = min(beta, valor)
            if alpha >= beta: #Elimino rama que sobra
                break
        return valor, mejor_mov

def jugador_turno():
    columna = int(input("Elige columna (1-7): ")) - 1 #No compruebo si el numero está fuera del rango, debe ser entre 1-7
    fila_disponible = obtener_fila(tablero, columna)
    tablero[fila_disponible][columna] = 'X'

def ia_turno():
    print("--JUEGA LA IA--")
    _, columna = minimax(tablero, 4, -math.inf, math.inf, True)
    fila_disponible = obtener_fila(tablero, columna)
    tablero[fila_disponible][columna] = 'O'
    print(f"IA coloca: {columna + 1}")

def jugar():
    while True:
        imprimir_tablero()
        #JUGADOR
        jugador_turno()
        if verificar_ganador_estado(tablero, 'X'):
            imprimir_tablero()
            print("¡HAS GANADO!")
            break
        if tablero_lleno(tablero):
            imprimir_tablero()
            print("¡EMPATE!")
            print("Mondongo")
            break
        #IA
        ia_turno()
        if verificar_ganador_estado(tablero, 'O'):
            imprimir_tablero()
            print("¡HAS PERDIDO, GANA LA IA")
            break
        if tablero_lleno(tablero):
            imprimir_tablero()
            print("¡EMPATE!")
            print("Mondongo")
            break

#JUEGO
jugar()
print("¡FINAL DE LA PARTIDA!")
