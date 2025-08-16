from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
keep_on = True
while keep_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        keep_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in ["latte", "espresso", "cappuccino"]:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Invalid choice, please try again.")