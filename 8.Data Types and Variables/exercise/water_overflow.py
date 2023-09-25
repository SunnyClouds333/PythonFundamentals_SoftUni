tank_capacity = 255
number_of_lines = int(input())
final_capacity = 0

for i in range(1, number_of_lines + 1):
    current_liters_of_water = int(input())
    if current_liters_of_water > tank_capacity:
        print("Insufficient capacity!")
        continue
    tank_capacity -= current_liters_of_water
    final_capacity = 255 - tank_capacity


print(final_capacity)