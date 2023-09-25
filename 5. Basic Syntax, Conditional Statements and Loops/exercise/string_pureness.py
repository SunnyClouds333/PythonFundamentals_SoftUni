
str_num = int(input())

for i in range(1, str_num + 1):
    text = input()
    part_one = ','
    part_two = '.'
    part_three = '_'

    if part_one in text or part_two in text or part_three in text:
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")




