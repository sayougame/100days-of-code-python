

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
    "money": 0
}


def report(resources):
    for key, value in resources.items():
        if key == "water":
            unit = "ml"
        elif key == "milk":
            unit = "ml"
        elif key == "coffee":
            unit = "g"
        elif key == "money":
            unit = "$"


def check_order(user_order, MENU):
    if user_order == "espresso":



        print(f"{key.capitalize()}: {value}{unit}")
machine_on = True
while machine_on == True:

    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "off":
        break
    elif user_order == "report":
        report(resources)
    elif user_order == "espresso" or user_order == "latte" or "user_order == cappuccino":

