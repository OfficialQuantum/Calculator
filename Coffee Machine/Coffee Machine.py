# TODO 1. Prompt the use by asking what they would like
# TODO 2. Turn off the machine by replying off to the prompt
# TODO 3. create a print for report
# TODO 4. check if resources are sufficient
# TODO 5. process the coins
# TODO 6. Check if transaction is successful
from menu_page import menu, resources
import math


def is_resources_sufficient(order_ingredients):
    """Compare the order ingredients with the resources to check if the resources are sufficient"""
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print("Sorry there is not enough water.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    coins = math.ceil(quarters + dimes + nickles + pennies)
    return coins


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f'Here\'s ${change} in change.')
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredient):
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]
    print(f"Here is your {drink_name}. Enjoy!")


profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: ${profit}')
    else:
        drink = menu[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



