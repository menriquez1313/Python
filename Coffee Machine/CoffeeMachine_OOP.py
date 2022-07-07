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


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on == True:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    
    #If user chooses off, coffee machine will shutdown.
    if choice == "off":
        print("Shutting off...")
        time.sleep(2)
        print("Have a nice day! ")
        is_on = False
    
    #Report will show what ingredients are left and how much money has been made. 
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        
    #This processes the payment and makes drinks. 
    #if insufficient with ingredients and/or payment, machine will not continue. 
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                print("Making Drink! Please wait...")
                time.sleep(3)
                coffee_maker.make_coffee(drink)