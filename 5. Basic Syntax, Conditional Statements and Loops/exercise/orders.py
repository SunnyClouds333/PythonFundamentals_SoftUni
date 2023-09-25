orders_count = int(input())
price_coffee = 0
total_price = 0

for i in range(1, orders_count + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or days < 1 or capsules_per_day < 1:
        continue
    if price_per_capsule > 100.00 or days > 31 or capsules_per_day > 2000:
        continue

    price_coffee = (price_per_capsule * capsules_per_day) * days
    print(f"The price for the coffee is: ${price_coffee:.2f}")
    total_price += price_coffee

print(f"Total: ${total_price:.2f}")