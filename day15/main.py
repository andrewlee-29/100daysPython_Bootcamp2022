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
is_on = True
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def checkresourece(selection_ingredients):
    for item in selection_ingredients:
        if (selection_ingredients[item] > resources[item]):
            print(f"Sorry! There is not enough {item}.")
            return False
        return True


def coin_process(cost):
    quarters= int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    total =0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies
    if (cost > total):
        print("not enough money")
    else:
        if(total>cost):
            print(f"Here is the change{total-cost}")
        print("making coffee")
        global profit
        profit = profit + cost


def make_coffee(selection_ingredients):
    for item in selection_ingredients:
        resources[item] = resources[item]-selection_ingredients[item]

# testing
while is_on:
    selection_input = input("What would you like?(espresso/latte/cappuccino): ")
    if selection_input == "off":
        is_on = False
    elif selection_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"profit:${profit}")
    elif selection_input
    else:
        print("input detected")
        loaddata = MENU[selection_input]
        if checkresourece(loaddata["ingredients"]):
            print("checked")
            coin_process(loaddata["cost"])
            make_coffee(loaddata["ingredients"])
            print(f"Here is your {selection_input}. Enjoy!!")
        else:
            print("back to the menu")