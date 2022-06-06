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

def sufficient(coffee):
    for items in coffee:
        if coffee[items] > resources[items]:
            print("Sorry! Insufficient ingredients!")
            return False
    return True
is_on = True
while is_on == True:
    choice = input("What would you like? (espresso, latte, cappuccino) ")
    
    if choice == "off":
        print("Have a nice day! ")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}g.")
        print(f"Money: ")
    else:
        drink = MENU[choice]
        if sufficient(drink["ingredients"]):
            print("It works!")