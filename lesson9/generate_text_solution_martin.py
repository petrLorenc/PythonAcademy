import os
import random

def get_bigrams(filedir): # from class
    dirname = os.path.dirname(__file__)
    filename = '{}{}{}'.format(dirname,os.path.sep, filedir)
    with open(filename, "r", encoding="utf-8") as f:
        data = " ".join(f.readlines()).lower().split(" ")
    bigrams = [(k.strip(), v.strip()) for k,v in zip(data, data[1:]) if k.strip() and v.strip()]
    return bigrams

def generate_text(word: str, length: int) -> print: # from class
    bigrams = get_bigrams('book.txt')
    result = word
    for _ in range (length):
        scope = []
        for bigram in bigrams:
            if bigram[0] == word:
                scope.append(bigram)
        word = random.choice(scope)[1]
        result += ' ' + word
    print (result)