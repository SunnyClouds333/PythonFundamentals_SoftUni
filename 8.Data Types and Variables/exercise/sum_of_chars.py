number_of_letters = int(input())
total_sum = 0
for i in range(1, number_of_letters +1):
    letter = input()
    value_ascii = ord(letter)
    total_sum += value_ascii
print(f'The sum equals: {total_sum}')
