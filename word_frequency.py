import re
from collections import Counter

def word_frequency(sentence):
    words = re.findall(r"\b[\w']+\b", sentence.lower()) # use regex to get a list of sentence substrings, including appostrophes
    word_frequency = Counter(words)  # create a Counter object to auto-count word frequencies from the words list
    return dict(word_frequency)  # convert the Counter object to a regular dictionary

sentence = "This is a test sentence? I'm sure this is a test sentence."

print(word_frequency(sentence))  # {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2, "i'm": 1, 'sure': 1}
