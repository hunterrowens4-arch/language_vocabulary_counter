import re
from collections import Counter

# get input from user
while True:
    filename = input('Enter the filename: ')
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        break
    except:
        print('No file was found at that address.')
        continue

# extract words using regex (removes punctuation) and count them
words = re.findall(r"\b\w+(?:'\w+)*\b", text, flags=re.UNICODE)
counts = Counter(words)

# read stop words from file and create a set for faster lookup
while True:
    language = input(
    'What language is the file in?\nSpanish = "s"\nRussian = "r"\n>>').strip().lower()
    if language == 's':
        with open('stop_words/stop_words_sp.txt', 'r', encoding='utf-8') as f:
            stop_words = {line.strip().lower() for line in f if line.strip()}
        break
    elif language == 'r':
        with open('stop_words/stop_words_ru.txt', 'r', encoding='utf-8') as f:
            stop_words = {line.strip().lower() for line in f if line.strip()}
        break
    else:
        print('Invalid input, please enter a valid language selection (s/r).')
        continue

# read known words from file and create a set for faster lookup
while True:
    filter_list = input('Would you like to use a "Known Words" filter? (y/n): ').lower()
    if filter_list == 'y':
        if language == 'r':
            with open('stop_words/known_words_ru.txt', 'r', encoding='utf-8') as f:
                known_words = {line.strip().lower() for line in f if line.strip()}
            break
        elif language == 's':
            with open('stop_words/known_words_sp.txt', 'r', encoding='utf-8') as f:
                known_words = {line.strip().lower() for line in f if line.strip()}
            break
    elif filter_list == 'n':
        known_words = {}
        break
    else:
        print('Invalid input. Please enter "y" or "n".')
        continue

# print word counts excluding stop words
print('\nVocabulary list (filtered):\n')
for word, count in counts.most_common():
    if word not in stop_words and word not in known_words:
        print(f'{word}: {count}')
