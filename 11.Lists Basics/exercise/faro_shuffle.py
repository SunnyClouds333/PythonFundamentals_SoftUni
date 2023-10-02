list_of_cards = input().split(" ")
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    middle_index = int(len(list_of_cards) // 2)
    left_part = list_of_cards[:middle_index]
    right_part = list_of_cards[middle_index:]
    shuffled_cards = []
    for card in range(len(left_part)):

        shuffled_cards.append(left_part[card])
        shuffled_cards.append(right_part[card])
        list_of_cards = shuffled_cards

print(shuffled_cards)




