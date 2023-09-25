first_number = int(input())
second_number = int(input())

for num in range(first_number, second_number + 1):
    num_as_ascii = chr(num)
    print(num_as_ascii, end= " ")

