MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50 ,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money: int = 0


def report():
    print(f"""
    water: {resources["water"]}ml
    milk: {resources["milk"]}ml
    coffee: {resources["coffee"]}g
    money: ${money}
    """)


def coin_calculator(coffee):
    print("Please enter coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    result = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
    if result >= MENU[coffee]["cost"]:
        return result - MENU[coffee]["cost"]
    else :
        return None


def check_resources(coffee):
    for key, value in resources.items():
        if resources[key] < MENU[coffee]["ingredients"][key]:
            return False
    return True


def make_coffee(coffee):
    if check_resources(coffee):
        change = coin_calculator(coffee)
        if change or change==0:
            for key, value in resources.items():
                resources[key] = resources[key] - MENU[coffee]["ingredients"][key]
            print(f"Here is your change of ${change}")
            print(f"Here is your {coffee}. Enjoy")
            global money
            money += MENU[coffee]["cost"]
        else:
            print("Sorry, not enough money. Money refunded")
    else:
        print("Sorry, there is not enough water")


state = True
while state:
    prompt = input(
        f"What would you like?\nespresso - ${MENU['espresso']['cost']}\nlatte - ${MENU['latte']['cost']}\ncappuccino - ${MENU['cappuccino']['cost']}\n")
    if prompt == "report":
        report()
    elif prompt == "off":
        exit()
    else:
        make_coffee(prompt)
