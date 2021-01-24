

import random


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
# TODO: analyze which words can follow other words
# Your code here
corpus = words.split()

def pair_words(text):
    for word in range(len(text)-1):
        yield (text[word], text[word + 1])

pairs = pair_words(corpus)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

# TODO: construct 5 random sentences
# Your code here
def random_sentance(num):
    first_word = random.choice(corpus)

    while first_word.islower():
        first_word = random.choice(corpus)

    chain = [first_word]

    n_words = num

    for i in range(n_words):
        chain.append(random.choice(word_dict[chain[-1]]))

    return " ".join(chain)

print(random_sentance(1))
print(random_sentance(10))
print(random_sentance(14))
print(random_sentance(16))
print(random_sentance(18))
print(random_sentance(20))