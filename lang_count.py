import re
from collections import Counter

# get input from user
filename = input('Enter the filename: ')

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read().lower()

# extract words using regex (removes punctuation) and count them
words = re.findall(r"\b\w+(?:'\w+)*\b", text, flags=re.UNICODE)
counts = Counter(words)

# read stop words from file and create a set for faster lookup
with open('stop_words/stop_words_sp.txt', 'r', encoding='utf-8') as f:
    stop_words = {line.strip().lower() for line in f if line.strip()}

# print word counts excluding stop words
print('\nVocabulary list (filtered):\n')
for word, count in counts.most_common():
    if word not in stop_words:
        print(f'{word.title()}: {count}')
