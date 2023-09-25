
divisor = int(input())
boundary = int(input())
largest_int = 0

for i in range(1, boundary + 1):

    if i % divisor == 0 and i <= boundary and i > 0:
        largest_int = i


print(largest_int)




