factor = int(input())
count = int(input())
numbers_list = []

for number in range(1, count + 1):
    num = number * factor
    numbers_list.append(num)

print(numbers_list)
