"""This is a Coffee Machine OOP Ver. !
There are 4 selections: Espresso, Latte, Cappuccino, and Report. 
Report will allow the user to check on the Resources.
Resources will update for every drink bought. """

from importlib.resources import is_resource
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

#Coffee Menu
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
"""

#These are the limited resources. 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

"""
#checks if there is enough resources
def sufficient(coffee):
    for items in coffee:
        if coffee[items] > resources[items]:
            print("Sorry! Insufficient ingredients!")
            return False
    return True

#Checks if the user has enough money
def money(price):
    quar = float(input("How many quarters? "))
    dim = float(input("How many dimes? "))
    nic = float(input("How many nickels? "))
    penn = float(input("How many pennies? "))
    
    total = round((quar * .25) + (dim * .10) + (nic * .05) + (penn * .01),2)
    print(f"You have paid is ${total}")
    print("...")
    if total < price:
        print("Insufficient Funds!")
        return False
    print(f"Your change is ${round(total - price,2)}")
    rec_money = resources.get("money")
    resources["money"] = rec_money + total
    return True

#updates the resources after payment   
def make_coffee(ingredients):
     for items in ingredients:
        resources[items] = resources[items] - ingredients[items]
        #print(ingredients[items]) #test to see if resources are updating
 """    

menu = Menu()
#menu_item = Menu()
coffee_maker = CoffeeMaker() #resources
money_maker = MoneyMachine()

is_on = True
while is_on == True:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    
    if choice == "off":
        print("Shutting off...")
        #time.sleep(2)
        print("Have a nice day! ")
        is_on = False
    elif choice == "report":
        """
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}g.")
        print(f"Money:${resources['money']}")
        """
        print(coffee_maker.report())
        print(money_maker.report())
    else:
        """
        drink = MENU[choice]
        if sufficient(drink["ingredients"]):
            if money(drink["cost"]):
                print("Making coffee!..... Please wait!")
                make_coffee(drink["ingredients"])
                time.sleep(3)
                print(f"Here is your {choice}!")
        """
        drink = menu.find_drink()
        