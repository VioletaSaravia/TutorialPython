dic = ["a", "b", "c", "d", "e", "f", "g", "h",
       "i", "j", "k", "l", "m", "n", "ñ", "o",
       "p", "q", "r", "s", "t", "u", "v", "w",
       "x", "y", "z"]

pantalla_inicial = "=== BIENVENIDO A CAESAR CIPHER ==="


def menu():
    print(pantalla_inicial)
    opcion = input("[C]odificar o [D]ecodificar? ")
    return accion(opcion)


def accion(modo):
    texto = input("Ingresar texto: \n")
    shift = int(input("Ingresar shift: \n"))
    print(cifrar(texto, shift, modo))
    continuar = input("Volver al menu? (y/n): ")
    if continuar == "y":
        return menu()
    else:
        return print("Chau!")


def cifrar(texto, shift, accion="C"):
    output = ''
    if accion == "D":
        shift *= -1
    for letra in texto:
        if letra not in dic:
            output += letra
        elif dic.index(letra) + shift < len(dic):
            output += dic[dic.index(letra) + shift]
        else:
            output += dic[dic.index(letra) + shift - len(dic)]
    return output


menu()
