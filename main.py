from data import MENU, resources

# Variables
menu_choices = ["espresso", "latte", "cappuccino", "off", "report"]
units = ["ml", "ml", "g", "€"]
coins = ["quarters", "dimes", "nickles", "pennies"]
coins_value = [0.25, 0.10, 0.05, 0.01]
coins_sum = 0
# TODO turn these into methods
enough_resources = True
enough_money = True

# Functions
def input_off(x):
    return x == "off"

def input_report(x):
    return x == "report"

def show_report():
    for key in resources:
        print(f"{key.title()}: {resources[key]}")

def ask_for_money(i):
    insert_coins = float(input(f"How many {coins[i]}?: "))
    return insert_coins * coins_value[i]    

def update_resources(ingredients):
    for key in ingredients:
        resources[key] -= ingredients[key]


keep_going = True
while keep_going:
    # 1. Ask user what they would like (espresso/latte/cappuccino)
    user_coffee = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    while user_coffee not in menu_choices:
        user_coffee = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    # 2. Turn off the Coffee Machine with 'off' - secret word
    if input_off(user_coffee):
        print("Goodbye")
        keep_going = False
        break
    elif input_report(user_coffee):
        # 3. Print a report, shows the current resources (water, milk, coffee, money)
        show_report()
        # coffee_machine()
    else:
        coffee_cost = MENU[user_coffee]["cost"]
        coffee_ingredients = MENU[user_coffee]["ingredients"]
        # 4. Check if resources are sufficient - put details of requirements here
        for key in coffee_ingredients:
            if resources[key] - coffee_ingredients[key] < 0:
                print(f"Sorry there is not enough {key}")
                enough_resources = False

        if enough_resources:
            # 5. Process coins, should calculate gross of all coins inserted - using dollars:
            for i in range(0, 4):
                coins_sum += ask_for_money(i)
            coins_sum_round = round(coins_sum, 2)

            # 6. Check that the transaction is successful - did the user insert enough money? Refund excess or on failure
            cost_difference = coins_sum_round - coffee_cost
            if cost_difference < 0:
                print("Not enough money")
                enough_money = False
            else:
                update_resources(coffee_ingredients)
                resources["money"] += coffee_cost
                if cost_difference > 0:
                    refund = cost_difference            
                    print(f"\nHere is your refund of {refund}\n")

            if enough_money:
                # 7. Make the coffee, give a new report on resources
                show_report()
                # 8. Finally tell the user to enjoy their coffee
                print("Here is your coffee")
