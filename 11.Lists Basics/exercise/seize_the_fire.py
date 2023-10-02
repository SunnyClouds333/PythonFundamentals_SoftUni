fire_list = input().split("#")
total_water_amount = int(input())
put_out_fire = 0
effort = 0
total_put_out_cells = []


for item in fire_list:
    split_fire = item.split(' = ')
    type_fire = split_fire[0]
    water_needed_per_fire = int(split_fire[1])
    if total_water_amount < water_needed_per_fire:
        continue
    if type_fire == "High" and 81 <= water_needed_per_fire <= 125:
        effort += water_needed_per_fire * 0.25
        total_water_amount -= water_needed_per_fire
        put_out_fire += water_needed_per_fire
        total_put_out_cells. append(water_needed_per_fire)
    elif type_fire == "Medium" and 51 <= water_needed_per_fire <= 80:
        effort += water_needed_per_fire * 0.25
        total_water_amount -= water_needed_per_fire
        put_out_fire += water_needed_per_fire
        total_put_out_cells.append(water_needed_per_fire)
    elif type_fire == "Low" and 1 <= water_needed_per_fire <= 50:
        effort += water_needed_per_fire * 0.25
        total_water_amount -= water_needed_per_fire
        put_out_fire += water_needed_per_fire
        total_put_out_cells.append(water_needed_per_fire)

print('Cells:')
for fire_cell in total_put_out_cells:
    print(f" - {fire_cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {put_out_fire}")

