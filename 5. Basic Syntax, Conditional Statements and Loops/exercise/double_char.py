
print_result = ""


while True:
    command = input()

    if command == "End":
        break
    elif command == "SoftUni":
        continue

    for char in command:
        print_result += char*2

    print(print_result)
    print_result = ''


