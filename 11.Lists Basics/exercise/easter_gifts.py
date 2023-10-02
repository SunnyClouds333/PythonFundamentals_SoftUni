gifts_list = input().split(" ")


while True:
    command = input()
    split_command = command.split(" ")
    type_action = split_command[0]
    gift_type = split_command[1]
    if type_action == "OutOfStock":
        if gift_type in gifts_list:
            for index in range(len(gifts_list)):
                if gifts_list[index] == gift_type:
                    gifts_list[index] = "None"
    elif type_action == "Required":
        gift_index = int(split_command[2])
        if gift_index in range(len(gifts_list)):
            gifts_list[gift_index] = gift_type
    elif type_action == "JustInCase":
        gifts_list.pop()
        gifts_list.append(gift_type)
    if command == "No Money":
        break

final_list = []
for gift in gifts_list:
    if gift != "None":
        final_list.append(gift)

print(*final_list)
