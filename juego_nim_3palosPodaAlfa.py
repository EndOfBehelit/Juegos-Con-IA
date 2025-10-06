def mover_jugador(fichas_total):
    while True:
        try:
            movimiento = int(input("¿Cuántas fichas quieres tomar? (1 a 3): "))
            if movimiento not in [1, 2, 3]:
                print("Solo puedes tomar entre 1 y 3 fichas.")
            elif movimiento > fichas_total:
                print(f"No puedes tomar más fichas de las que quedan ({fichas_total}).")
            else:
                return movimiento
        except ValueError:
            print("Entrada inválida. Ingresa un número.")

# Minimax con poda alfa-beta
def minimax(fichas, es_max, alpha, beta):
    if fichas == 0:
        return -1 if es_max else 1  # Gana quien hizo el último movimiento

    if es_max:
        max_eval = -float('inf')
        for mov in range(1, 4):
            if fichas - mov >= 0:
                eval = minimax(fichas - mov, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Poda beta
        return max_eval
    else:
        min_eval = float('inf')
        for mov in range(1, 4):
            if fichas - mov >= 0:
                eval = minimax(fichas - mov, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Poda alfa
        return min_eval

def mover_ia(fichas):
    mejor_movimiento = None
    mejor_valor = -float('inf')

    for mov in range(1, 4):
        if fichas - mov >= 0:
            valor = minimax(fichas - mov, False, -float('inf'), float('inf'))
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = mov

    print(f"La IA toma {mejor_movimiento} ficha(s).")
    return mejor_movimiento

def jugar(fichas):
    print("¡Bienvenido al juego del Nim con IA (Minimax + poda alfa-beta)!\n")
    print("Quien toma la última ficha gana.\n")

    while fichas > 0:
        print("Fichas restantes:", fichas)

        # Turno de la IA
        movimiento_ia = mover_ia(fichas)
        fichas -= movimiento_ia
        if fichas == 0:
            print("La IA toma la última ficha. ¡Gana la IA!")
            break

        print("Fichas restantes:", fichas)

        # Turno del jugador
        movimiento_jug = mover_jugador(fichas)
        fichas -= movimiento_jug
        if fichas == 0:
            print("Tomas la última ficha. ¡Ganas tú!")
            break

# Ejecutar juego
jugar(10)
