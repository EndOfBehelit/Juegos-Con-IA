import random

def mover_jugador(fichas_total):
    while True:
        try:
            movimiento = int(input("¿Cuántas fichas quieres tomar? (1 o 2): "))
            if movimiento not in [1, 2]:
                print("Solo puedes tomar 1 o 2 fichas.")
            elif movimiento > fichas_total:
                print(f"No puedes tomar más fichas de las que quedan ({fichas_total}).")
            else:
                return movimiento
        except ValueError:
            print("Entrada inválida. Ingresa un número.")

def mover_ia(fichas_total):
    if fichas_total >= 2:
        movimiento = random.randint(1, 2)
    else:
        movimiento = 1
    print(f"La IA toma {movimiento} ficha(s).")
    return movimiento

def jugar(fichas):
    print("¡Bienvenido al juego del Nim! Quien tome la última ficha gana.\n")

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

# Ejecutar el juego
jugar(10)
