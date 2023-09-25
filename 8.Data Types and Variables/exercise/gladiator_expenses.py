lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_broken = lost_fight_count // 2
swords_broken = lost_fight_count // 3
shields_broken = lost_fight_count // (2 * 3)
armors_broken = shields_broken // 2
total_expenses = (helmets_broken * helmet_price)\
                 + (swords_broken * sword_price) + \
                 (shield_price * shields_broken) + \
                 (armors_broken * armor_price)

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
