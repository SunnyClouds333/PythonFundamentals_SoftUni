received_year = int(input())

while True:
    received_year += 1
    year_as_string = str(received_year)
    if len(year_as_string) == len(set(year_as_string)):
        break

print(received_year)