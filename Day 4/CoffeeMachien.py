"""What can be better than a cup of coffee during a break? A coffee that you don’t have to make yourself.
It’s enough to press a couple of buttons on the machine and you get a cup of energy; but first, 
we should teach the machine how to do it. In this project, you will work on programming a coffee
machine simulator. The machine works with typical products: coffee, milk, sugar, and plastic cups; 
if it runs out of something, it shows a notification. You can get three types of coffee: espresso, 
cappuccino, and latte. Since nothing’s for free, it also collects the money."""

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

profit = 0 # money in machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def isResourceSufficient(orderIngredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def processCoins():
    """Returns the total calcualted from coins inserted."""
    print("Please insert conis.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def isTransactionSuccessful(moneyReceived, drinkCost):
    """Return True when the payment is accepted, 
    or False if money is insufficient."""
    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False


def makeCoffee(drinkName, orderIngredients):
    """Deduct the required ingredients from the resources."""
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here is your {drinkName}, Enjoy!")


isOn = True

while isOn:
    choice = input("What would you like? (espresso, latte, cappuccino):  " ).lower()
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink['ingredients']):
            payment = processCoins()
            if isTransactionSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])

