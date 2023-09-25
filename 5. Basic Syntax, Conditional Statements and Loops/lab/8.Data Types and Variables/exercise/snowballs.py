number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snowball in range(1, number_of_snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    if 0 >= weight >= 1000 or 1 >= time >= 500 or 0 >= quality >= 100:
        continue

    value = int((weight / time) ** quality)

    if value > max_value:
        max_weight = weight
        max_time = time
        max_quality = quality
        max_value = value

print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")

