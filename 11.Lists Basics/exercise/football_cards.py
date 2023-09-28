cards = input()
cards_list = list(cards.split(" "))
team_a = 11
team_b = 11
game_terminated = False
first_team_sent_off_players = []
second_team_sent_off_players = []

for card in cards_list:
    if card in first_team_sent_off_players or card in second_team_sent_off_players:
        continue
    if "A" in card:
        team_a -= 1
        first_team_sent_off_players.append(card)
    elif "B" in card:
        team_b -= 1
        second_team_sent_off_players.append(card)
    if team_a < 7 or team_b < 7:
        game_terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if game_terminated:
    print("Game was terminated")