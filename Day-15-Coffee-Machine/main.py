from data import COIN, MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def make_coffee(command):
    global money
    for key in MENU[command]["ingredients"]:
        if resources[key] < MENU[command]["ingredients"][key]:
            print(
                f"{key} not enough. Money refunded.")
            return False

    money += MENU[command]["cost"]
    resources['water'] -= MENU[command]["ingredients"]["water"]
    resources["milk"] -= MENU[command]["ingredients"]['milk'] if 'milk' in MENU[command]["ingredients"] else 0
    resources["coffee"] -= MENU[command]["ingredients"]["coffee"]

    print(f"Here is your {command} ☕️. Enjoy!")


def show_report():
    print(
        f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}"
    )


def inputMoney():
    total_quarters = int(input("How many quarters?: "))
    total_dimes = int(input("How many dimes?: "))
    total_nickles = int(input("How many nickles?: "))
    total_pennies = int(input("How many pennies?: "))
    return (total_quarters * COIN["quarter"]) + (total_dimes * COIN["dime"]) + (
        total_nickles * COIN["nickel"]) * (total_pennies * COIN["penny"])


while True:
    command = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if command == "report":
        show_report()
    elif command == "off":
        break
    else:
        if command in MENU:
            total_money = inputMoney()
            if total_money >= MENU[command]['cost']:
                if total_money - MENU[command]['cost'] > 0:
                    if make_coffee(command) != False:
                        print(
                            f"Here is ${total_money - MENU[command]['cost']} in change")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Command not found")
