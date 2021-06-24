from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cafetera = CoffeeMaker()
dinero = MoneyMachine()

def main():
    """ Menu principal """	
    pedido = input("Qué quiere tomar? (espresso/latte/cappuccino): ")
    if pedido == 'off':
        return print("Adios!")
    if pedido == "report":
        print(cafetera.report())
        print(dinero.report())
    elif pedido in menu.get_items() and cafetera.is_resource_sufficient(menu.find_drink(pedido)):
        dinero.make_payment(menu.find_drink(pedido).cost)
        cafetera.make_coffee(menu.find_drink(pedido))
    return main()
        

main()