n = int(input())
my_list = []

for _ in range(n):
    number = int(input())
    my_list.append(number)

command = input()
filtered_list = []

if command == 'even':
    for num in my_list:
        if num % 2 == 0:
            filtered_list. append(num)
elif command == 'odd':
    for num in my_list:
        if num % 2 != 0:
            filtered_list. append(num)
elif command == 'negative':
    for num in my_list:
        if num < 0:
            filtered_list. append(num)
if command == 'positive':
    for num in my_list:
        if num >= 0:
            filtered_list. append(num)


print(filtered_list)