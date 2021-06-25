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
    elif pedido in menu.get_items():
        drink = menu.find_drink(pedido)
        if cafetera.is_resource_sufficient(drink):
            dinero.make_payment(drink.cost)
            cafetera.make_coffee(drink)
    return main()
        

main()
