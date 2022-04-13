
text = input("Text: ").split(" ")

word_to_count = {}
for i in range(len(text)):
    if text[i] in word_to_count:
        word_to_count[text[i]] += 1
    else:
        word_to_count.update({text[i]: 1})



