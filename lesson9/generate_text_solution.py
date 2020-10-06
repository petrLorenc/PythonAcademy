import random

with open("./book.txt", "r", encoding="utf-8") as f:
    data = " ".join(f.readlines()).lower().split(" ")

bigrams = [(k.strip(), v.strip()) for k, v in zip(data, data[1:]) if k.strip() and v.strip()]

def generate(word, steps=50):
    text = word

    for step in range(steps):
        possible_ways = [bigram[1] for bigram in bigrams if bigram[0] == word]
        if possible_ways:
            word = random.choice(possible_ways)
        else:
            word = random.choice([bigram[0] for bigram in bigrams])
        text += " " + word
    return text

print(generate(word="who"))
