import math
import time

AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[91m"
NORMAL = "\033[0m"

TABLERO_INICIAL = 12
MOVIMIENTOS_POSIBLES = [1, 2, 3]
PIEDRA = "🪨"

def mostrar_piedras(n):
    print("\n" + " ".join([PIEDRA for _ in range(n)]), f"({n} piedras)\n")

# - minimax(): función recursiva que simula todos los posibles estados del juego 
#   para determinar si una posición es ganadora o perdedora, asumiendo que ambos 
#   jugadores juegan de forma óptima.
# - jugada_IA(): utiliza minimax para elegir la mejor jugada posible para la IA 
#   en su turno, evaluando qué movimiento le ofrece la mayor probabilidad de victoria.
def minimax(piedras_restantes, es_turno_IA):
    if piedras_restantes == 0 and es_turno_IA:
        return -1 
    elif piedras_restantes == 0 and not es_turno_IA:
        return 1


    if es_turno_IA:
        mejor_valor = -float('inf')
        for mov in range(1, 4):
            if piedras_restantes - mov >= 0:
                valor = minimax(piedras_restantes - mov, False)
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float('inf')
        for mov in range(1, 4):
            if piedras_restantes - mov >= 0:
                valor = minimax(piedras_restantes - mov, True)
                mejor_valor = min(mejor_valor, valor)
        return mejor_valor


def jugada_IA(piedras_restantes):
    mejor_movimiento = None
    mejor_valor = -float('inf')

    for mov in range(1, 4):
        if piedras_restantes - mov >= 0:
            valor = minimax(piedras_restantes - mov, False)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = mov

    return mejor_movimiento

def jugar():
    piedras = TABLERO_INICIAL
    print(f"{AZUL}Bienvenido al juego de Nim. Recuerda que pierde quien quite la última piedra...{NORMAL}\n")
    turno_jugador = input(f"{AZUL}¿Quieres empezar tú? Si dices que no, empezará la IA (s/n): {NORMAL}").lower().strip() == 's'

    while piedras > 0:
        mostrar_piedras(piedras)
        if turno_jugador:
            while True:
                mov = int(input("Tu turno. ¿Cuántas piedras quieres quitar (1, 2 o 3)? "))
                if mov in MOVIMIENTOS_POSIBLES and mov <= piedras:
                    break
                else:
                    print(f"{ROJO}Movimiento inválido. No intentes hacer trampas{NORMAL}")
        else:
            print("Ahora es el turno de la IA...")
            time.sleep(2)
            print("La IA está pensando cuántas piedras quitar...")
            time.sleep(2)
            mov = jugada_IA(piedras)
            print(f"Finalmente, la IA retira {mov} piedra(s).")

        piedras = piedras - mov
        if piedras == 0:
            mostrar_piedras(piedras)
            print("-----------------------------")
            if turno_jugador:
                print(f"{VERDE}Has ganado. Has quitado la última priedra.{NORMAL}")
            else:
                print(f"{ROJO}Has perdido. La IA ha quitado la última piedra.{NORMAL}")
            break

        turno_jugador = not turno_jugador
        time.sleep(1)

if __name__ == "__main__":
    jugar()




