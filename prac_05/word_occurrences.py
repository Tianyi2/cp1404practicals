
text = input("Text: ").split(" ")

word_to_count = {}
for i in range(len(text)):
    if text[i] in word_to_count:
        word_to_count[text[i]] += 1
    else:
        word_to_count.update({text[i]: 1})

sorted_word_to_count = sorted(word_to_count.items())

for i in range(len(sorted_word_to_count)):
    print(f"{sorted_word_to_count[i][0]} : {sorted_word_to_count[i][1]}")

