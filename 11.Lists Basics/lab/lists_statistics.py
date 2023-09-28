n = int(input())
positives_list = []
negatives_list = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        positives_list.append(number)
    elif number < 0:
        negatives_list.append(number)

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")