from random import choice
MAZO_BASE = ([x for x in range(1, 11)] + ([10] * 3)) * 4
CARTAS_JUGADOR = "Tus cartas: "
CARTAS_PC = "Cartas de la computadora: "
CONT_MANO = "Robar otra corta? [y/n]: "
CONT_PART = "Jugar otra mano? [y/n]: "
GAME_OVER = "Volver a jugar? [y/n]: "
WIN = "Ganaste!"
LOSE = "Perdiste!"


# print(mazo)

# mazo.remove(1)
# print(mazo)
# mano = choice(mazo)
# print(mano)
# mazo.remove(mano)
# print(mazo)


def menu_principal():
    print("=== BIENVENIDX A BLACKJACK ===")
    partida()
    return


def partida():
    mazo = MAZO_BASE

    def robar_carta():
        nonlocal mazo
        if mazo == []:
            mazo = MAZO_BASE
        carta = choice(mazo)
        mazo.remove(carta)
        return carta

    def mano():
        mano_jugadorx = []
        mano_pc = []
        nueva_jugada = True
        while nueva_jugada:
            mano_jugadorx.append(robar_carta())
            mano_pc.append(robar_carta())  # En realidad, el croupier roba
            # dos cartas al comienzo y sólo muestra una. Y roba primero¿?
            if sum(mano_jugadorx) > 21:
                print(CARTAS_JUGADOR + str(mano_jugadorx))
                print(LOSE)
                return 0
            elif sum(mano_pc) > 21:
                print(CARTAS_JUGADOR + str(mano_jugadorx))
                print(WIN)
                return 1
            print(CARTAS_JUGADOR + str(mano_jugadorx))
            print(CARTAS_PC + str(mano_pc))
            nueva_jugada = True if input(CONT_MANO) == "y" else False
        else:
            while sum(mano_pc) <= 16:
                mano_pc.append(robar_carta())
            else:
                print(CARTAS_PC + str(mano_pc))
                if sum(mano_pc) >= 21 or sum(mano_pc) < sum(mano_jugadorx):
                    print(WIN)
                    return 1
                else:
                    print(LOSE)
                    return 0
        return

    victorias = 0
    derrotas = 0
    nueva_mano = True
    while nueva_mano:
        if mano():
            victorias += 1
        else:
            derrotas += 1
        nueva_mano = True if input(CONT_PART) == "y" else False

    print("Fin del Juego")      # Tendría que estar en menu_principal maybe¿?¿?
    print("Tus victorias: " + str(victorias))
    print("Tus derrotas: " + str(derrotas))

    if input(GAME_OVER) == "y":
        partida()
    print("Adios!")             # Hasta acá
    return


menu_principal()
