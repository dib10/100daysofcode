from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

money_machine = MoneyMachine()
money_machine.report()

coffe_maker = CoffeeMaker()
coffe_maker.report()

is_on = True

while is_on:
