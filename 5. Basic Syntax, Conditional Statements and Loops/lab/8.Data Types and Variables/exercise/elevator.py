number_of_people = int(input())
capacity_per_round = int(input())
courses_counter = 0

while number_of_people > 0:
    remaining_people = int(number_of_people - capacity_per_round)
    number_of_people = remaining_people
    courses_counter += 1
    if remaining_people < 0:
        break
print(courses_counter)
