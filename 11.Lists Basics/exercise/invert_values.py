numbers = input()
list_as_str = list(numbers.split(" "))
number_list = [int(i) for i in list_as_str]
opposite_list = []
for num in number_list:
    opposite_num = num * - 1
    opposite_list.append(opposite_num)

print(opposite_list)