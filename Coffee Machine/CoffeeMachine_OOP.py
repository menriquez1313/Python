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


#These are the limited resources. 


menu = Menu()
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
        print(coffee_maker.is_resource_sufficient(drink))
        