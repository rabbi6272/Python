from menu import MENU, RESOURCES

income = 0
again = True

# def check_price(coffee_name):
#     price = MENU[coffee_name]["cost"]
#     input_money = int(input(f"The price of your coffee is {price}$. Enter money to buy it: "))
#     if input_money < price:
#         return print("Please enter sufficient money.")
#     elif input_money > price:
#         income += price
#         change = input_money - price
#         return print(f"Here is your change {change}$")
#     else:
#         income += price
#         return print(f"Here is your change {coffee_name}")
#     print(income)

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > RESOURCES[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name):
    """Deduct the required ingredients from the resources."""
    order_ingredients = MENU[drink_name]["ingredients"]
    for item in order_ingredients:
        RESOURCES[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def process(name):
    global income
    price = MENU[name]["cost"]
    input_money = int(input(f"The price of your coffee is {price}$. Enter money to buy it: "))
    if input_money < price:
        return print("Please enter sufficient money.")
    elif input_money > price:
        if not is_resource_sufficient(MENU[name]["ingredients"]):
            return
        income += price
        change = input_money - price
        print(f"Here is your change {change}$")
        make_coffee(name)
    else:
        if not is_resource_sufficient(MENU[name]["ingredients"]):
            return
        income += price
        make_coffee(name)


while again:
    coffee_name = input("Enter coffee name: ").lower()
    if coffee_name == "resources":
        print(RESOURCES)
    elif coffee_name == "income":
        print(income)
    else:
        if is_resource_sufficient(MENU[coffee_name]["ingredients"]):
            process(coffee_name)
        again = False
