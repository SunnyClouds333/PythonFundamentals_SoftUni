budget = int(input())
total_amount = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    current_amount = int(command)
    total_amount += current_amount

    if total_amount > budget:
        print("You went in overdraft!")
        break