MENSAJE_INICIAL = "=== BIENVENIDX A SUBASTA SECRETA ==="
PEDIR_NOMBRE = "Cuál es tu nombre? "
PEDIR_PUJA = "Cuál es tu puja? $"
CONTINUAR = "Agregar otra puja? (y/[N]) "
REINICIAR = "Comenzar otra subasta? (y/[N]) "
ADIOS = "Nos vemos!"


def menu_principal():
    print(MENSAJE_INICIAL)
    pujas = {}
    pujas = pujas | agregar_puja()
    # Creo que esto replaza pujas con el mismo nombre
    # (i.e. pares con la misma key)
    # TODO: varios valores para un mismo nombre¿?
    cont = input(CONTINUAR)
    while cont == "y":
        # TODO: LIMPIAR PANTALLA
        pujas = pujas | agregar_puja()
        cont = input(CONTINUAR)
    else:
        print(pujas)
        ganadorx = calcular(pujas)
        print("Ganó " + ganadorx[0] + " con una puja de $" + ganadorx[1])
    if input(REINICIAR) == "y":
        return menu_principal()
    else:
        return print(ADIOS)


def agregar_puja():
    return {input(PEDIR_NOMBRE): input(PEDIR_PUJA)}


def calcular(pujas):
    ganadorx = ""
    puja_ganadorx = 0
    for nombre, puja in pujas.items():
        if puja > ganadorx:
            ganadorx = nombre
            puja_ganadorx = puja
    return (ganadorx, puja_ganadorx)


menu_principal()
