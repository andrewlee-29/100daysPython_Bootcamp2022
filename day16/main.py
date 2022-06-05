from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on=True
m = Menu()
c = CoffeeMaker()
mm = MoneyMachine()
while(is_on):
    user_input = input(f"Hi, What do you want? ({m.get_items()}report/off) ")

    if (user_input == "report"):
        c.report()
        mm.report()
    elif (user_input == "off"):
        is_on = False
    else:
        user_item = m.find_drink(user_input)
        if c.is_resource_sufficient(user_item) and mm.make_payment(user_item.cost):
            c.make_coffee(user_item)

