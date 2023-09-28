n = int(input())
magic_word = input()
my_list = []
final_list = []

for sentence in range(n):
    sentences = input()
    my_list.append(sentences)
print(my_list)

for current_string in my_list:
    if magic_word in current_string:
        final_list.append(current_string)

print(final_list)
