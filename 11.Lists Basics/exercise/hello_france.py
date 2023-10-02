input_list = input().split("|")
given_budget = float(input())
train_ticket = 150
profit = 0
clothes_max_price = 50.0
shoes_max_price = 35
accessories_max_price = 20.5
new_price = 0
total_of_new_prices = 0
new_budget = 0
list_new_prices = []


for item in input_list:
    item_to_buy, item_price = item.split("->")
    item_price = float(item_price)
    if given_budget < item_price:
        continue
    if item_to_buy == "Clothes":
        if item_price > clothes_max_price:
            continue
        given_budget -= item_price
    elif item_to_buy == "Shoes":
        if item_price > shoes_max_price:
            continue
        given_budget -= item_price
    elif item_to_buy == "Accessories":
        if item_price > accessories_max_price:
            continue
        given_budget -= item_price

    if item_to_buy == "Clothes":
        new_price = item_price * 1.4
        list_new_prices.append(new_price)
        total_of_new_prices += new_price
        profit += new_price - item_price
    elif item_to_buy == "Shoes":
        new_price = item_price * 1.4
        list_new_prices.append(new_price)
        total_of_new_prices += new_price
        profit += new_price - item_price
    elif item_to_buy == "Accessories":
        new_price = item_price * 1.4
        list_new_prices.append(new_price)
        total_of_new_prices += new_price
        profit += new_price - item_price

    new_budget = given_budget + total_of_new_prices

for price in list_new_prices:
    print(f"{price:.2f}", end = " ")
print()
print(f"Profit: {profit:.2f}")
if new_budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
