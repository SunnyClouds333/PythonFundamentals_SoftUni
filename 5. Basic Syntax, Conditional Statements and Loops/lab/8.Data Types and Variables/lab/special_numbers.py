# number = int(input())
#
# for num in range(1, number + 1):
#     current_num_as_str = str(num)
#     digits_sum = 0
#     for digit in current_num_as_str:
#         digits_sum += int(digit)
#     is_special = False
#     if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
#         is_special = True
#     print(f"{num} -> {is_special}")

number = int(input())
is_special = False

for i in range(1, number + 1):
    first = i % 10
    second = i // 10
    digit_sum = first + second
    is_special = False
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True

    print(f"{i} -> {is_special}")