list_of_numbers = [int(i) for i in list(input().split(", "))]
# int_list = [int(i) for i in string_list]    // combined with list making above

number_of_beggars = int(input())
final_sum = []
start_index = 0

while start_index < number_of_beggars:
    sum_for_current_beggar = 0
    for curr_index in range(start_index, len(list_of_numbers), number_of_beggars):
        sum_for_current_beggar += list_of_numbers[curr_index]
    final_sum.append(sum_for_current_beggar)
    start_index += 1
print(final_sum)

