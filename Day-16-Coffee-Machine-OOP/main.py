from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    options = menu.get_items()
    command = input(f"What would you like? ({options}): ")

    if command == "off":
        break
    elif command == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(command)
        isPaymentValid = money_machine.make_payment(drink.cost)
        if isPaymentValid:
            if coffee_maker.is_resource_sufficient(drink):
                coffee_maker.make_coffee(drink)
