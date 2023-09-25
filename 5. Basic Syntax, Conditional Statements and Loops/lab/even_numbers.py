count_numbers = int(input())

for num in range(count_numbers):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        break

else:
    print("All numbers are even.")