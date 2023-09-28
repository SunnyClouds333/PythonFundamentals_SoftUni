cards = input()
cards_list = list(cards.split(" "))
team_a = 11
team_b = 11
game_terminated = False
set_of_list = set(cards_list)

for card in set_of_list:
    if "A" in card:
        team_a -= 1
    elif "B" in card:
        team_b -= 1
    if team_a < 7 or team_b < 7:
        game_terminated = True
        continue

print(f"Team A - {team_a}; Team B - {team_b}")
if game_terminated:
    print("Game was terminated")