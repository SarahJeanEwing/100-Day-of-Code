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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0
keep_on = True

def return_unit_of_measure(resource):
    if resource == "water" or resource == "milk":
        return "ml"
    elif resource == "coffee":
        return "g"


def check_resources(ingredients):
    for item in ingredients:
        if resources[item] - ingredients[item] <= 0:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return total


def adjust_resources(ingredients):
    global money
    money += drink['cost']
    for item in ingredients:
        resources[item] -= ingredients[item]



while keep_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        keep_on = False
    elif choice == "report":
        for resource in resources:
            unit = return_unit_of_measure(resource)
            print(f"{resource.capitalize()}: {resources[resource]}{unit}")
        print(f"Money: {'${:,.2f}'.format(money)}")
    elif choice in ["espresso", "latte", "cappuccino"]:
        drink = MENU[choice]
        enough_resources = check_resources(drink["ingredients"])
        if enough_resources:
            payment = process_coins()
            if payment < drink['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                adjust_resources(drink["ingredients"])
                change = payment - drink['cost']
                print(f"Here is {'${:,.2f}'.format(change)} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
    else:
        print("That is not a valid choice, please try again.")

