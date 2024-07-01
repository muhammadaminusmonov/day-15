from data import MENU, resources


def report_recourse(recourse):
    """Returns all the remaining recourses"""
    message = (f"Water: {recourse['water']}ml\nMilk: {recourse['milk']}ml\n"
               f"Coffee: {recourse['coffee']}g")

    if len(recourse) > 3:
        message += f"\nMoney: ${recourse['money']}"
    return message


def check_resources_sufficient(request, recourse):
    """Checks if the all recourses are enough. Returns True if is enough. If not enough, returns False"""
    ingredients = request["ingredients"]

    for key in ingredients:
        if recourse[key] < ingredients[key]:
            print(f"Sorry, there is not enough {key}")
            return False
    return True


def get_coins():
    """Gets coins from user and returns total amount"""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many nickles?: "))

    total_amount = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return total_amount


def update_resources(coffee, supplies):
    """Updates resources "dictionary" """
    if len(supplies) < 4:
        supplies["money"] = coffee["cost"]
    else:
        supplies["money"] += coffee["cost"]

    for key in coffee["ingredients"]:
        supplies[key] -= coffee["ingredients"][key]


def game():
    should_continue = True

    while should_continue:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "off":
            should_continue = False
        elif order == "report":
            print(report_recourse(resources))
        elif order == "espresso" or order == "latte" or order == "cappuccino":

            ordered_coffee = MENU[order]
            check_resource_sufficient = check_resources_sufficient(ordered_coffee, resources)

            if check_resource_sufficient:
                money = get_coins()
                cost = ordered_coffee["cost"]

                if money < cost:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    change = round(money - ordered_coffee["cost"], 2)
                    print(f"Here is ${change} dollars in change.")
                    update_resources(ordered_coffee, resources)
                    print(f"Here is your {order}. Enjoy!")

        else:
            print("Entered wrong variable")


game()
