quantity_to_buy = int(input())
days_till_christmas = int(input())
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garland = 3
price_tree_lights = 15
budget_needed = 0
christmas_spirit = 0

for current_day in range(1, days_till_christmas + 1):
    if current_day % 11 == 0:
        quantity_to_buy += 2

    if current_day % 2 == 0:
        budget_needed += quantity_to_buy * price_ornament_set
        christmas_spirit += 5
    if current_day % 3 == 0:
        budget_needed += quantity_to_buy * (price_tree_skirt + price_tree_garland)
        christmas_spirit += 13
    if current_day % 5 == 0:
        budget_needed += quantity_to_buy * price_tree_lights
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        budget_needed += price_tree_skirt + price_tree_garland + price_tree_lights

if days_till_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {budget_needed}")
print(f"Total spirit: {christmas_spirit}")

