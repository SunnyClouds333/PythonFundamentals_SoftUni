budget = float(input())
price_per_kg_flour = float(input())
price_per_pack_eggs = price_per_kg_flour * 0.75
price_per_liter_milk = price_per_kg_flour * 1.25
loaves_made = 0
loaf_counter = 0
colored_eggs = 0
price_per_loaf = price_per_pack_eggs + price_per_kg_flour + (price_per_liter_milk / 4)

while budget > price_per_loaf:
    loaf_counter += 1
    budget -= price_per_loaf
    colored_eggs += 3

    if loaf_counter % 3 == 0:
        colored_eggs -= loaf_counter - 2


print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")




