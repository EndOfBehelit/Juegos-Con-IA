#Jugadas posibles
jugadas = ['piedra', 'papel', 'tijera']

#Clacular el resultado
def calcularValor(max_jugada, min_jugada):
    #Puede devolver 0 para el caso del empate
    #1 para el caso de la victoria del jugador
    #-1 para el caso de la derrota del jugador
    if (max_jugada == min_jugada):
        return 0
    elif (max_jugada == 'piedra' and min_jugada == 'tijera' 
          or max_jugada == 'papel' and min_jugada == 'piedra' 
          or max_jugada == 'tijera' and min_jugada == 'papel'):
        return 1
    else:
        return -1 #GANA LA IA

#Función Minimax: Elige la jugada de la IA
def minimax(max_jugada):
    #Recorrer el bucle de opciones posibles y elegir la mejor opción
    #La de menor valor
    results = [] #ARRAY CON LOS RESULTADOS DE LAS 3 COMBINACIONES POSIBLES
    for i in jugadas:
        results.append(calcularValor(max_jugada, i))

    return jugadas[results.index(min(results))] 

#Inicio
max_jugada = input("Elige tu jugada: ")

if max_jugada in jugadas:
    min_jugada = minimax(max_jugada)
    print("Min elige:", min_jugada)
    
