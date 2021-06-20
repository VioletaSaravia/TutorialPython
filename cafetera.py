"""
Cafetera sin OOP
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    for resource, amount in RESOURCES.items():
        print('{}: {}'.format(resource, amount))
    return menu()

def hacer_cafe(cafe):
    for resource, amount in RESOURCES.items():
        #breakpoint()
        if resource in MENU[cafe]['ingredients'].keys():
            #breakpoint()
            if amount <= MENU[cafe]['ingredients'][resource]:
                RESOURCES[resource] -= MENU[cafe]['ingredients'][resource]
            else:
                return False
    print('Aquí está su {}.'.format(cafe)) # poner en menú
    return True


def dinero(cafe):
    veinticinco = int(input("Monedas de 25?: "))
    diez = int(input("Monedas de 10?: "))
    cinco = int(input("Monedas de 5?: "))
    cent = int(input("Monedas de un centavo?: "))
    total = (veinticinco * 25 + diez * 10 + cinco * 5 + cent) / 100

    if total >= MENU[cafe]['cost']:
        cambio = total - MENU[cafe]['cost']
        print('Su cambio es ${}.'.format(cambio))
        return True
#     print('Su dinero es insuficiente') # poner en menú
    return False

def menu():
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == 'report':
        return report()
    if prompt == 'off':
        return print("Adios!")
    if dinero(prompt):
        if not hacer_cafe(prompt):
            print('Insuficientes recursos.')
    return menu()

menu()
