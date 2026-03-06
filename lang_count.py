import re
import shutil
from collections import Counter

# get user action choice
while True:
    choice = input("""
Welcome to the Vocab Mining Tool!

What would you like to do?
> Mine = Isolate study worthy vocab from a text file
> Add  = Add words to your Known Words List(s)
> Exit = Close the program

>>""").lower().strip()
    if choice == 'mine':
        while True:
            filename = input('\nEnter the filename:\n>>')
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                break
            except:
                print('No file was found at that address.')
                continue
        words = re.findall(r"\b\w+(?:'\w+)*\b", text, flags=re.UNICODE)
        counts = Counter(words)
        language = input('\nWhat language is the file in?\n>>').strip().lower()
        stop_words = []
        try:
            with open(f'stop_words/stop_words_{language}.txt', 'r', encoding='utf-8') as f:
                stop_words = [line.strip().lower() for line in f if line.strip()]
        except:
            print('WARNING: No Stop Words list was found in that language choice.')
            continue_choice = input('Continue without a Stop Words list?\n>>')
            if continue_choice == 'n':
                exit()

        filter_list = input('\nWould you like to use a "Known Words" filter? (y/n)\n>>').lower()
        while True:
            if filter_list == 'y':
                try:
                    with open(f'stop_words/known_words_{language}.txt', 'r', encoding='utf-8') as f:
                        known_words = [line.strip().lower() for line in f if line.strip()]
                        break
                except:
                    print('WARNING: No Known Words list was found for that language choice.\nContinuing without a Known Words list.')
                    known_words = []
                    break
            elif filter_list == 'n':
                known_words = []
                break
            else:
                print('Invalid input. Please respond with "y" or "n".')
        print('\nVocabulary list (filtered):\n')
        for word, count in counts.most_common():
            if word not in stop_words and word not in known_words:
                print(f'{word}: {count}')
    elif choice == 'add':
        language = input('\nWhich Known Words list would you like to add to?\n>>').lower().strip()
        try:
            with open(f'stop_words/known_words_{language}.txt', 'r', encoding='utf-8') as f:
                known_words = [line.strip().lower() for line in f if line.strip()]
        except:
            known_words = []
        add_words_str = input('\nWhat words would you like to add to the list? Separate the words only with spaces.\n>>').lower().strip()
        add_words = [add_words_str.split()]
        for word in add_words:
            if word in known_words:
                continue
            known_words.extend(word)
            known_words.sort()
        try:
            shutil.copy(f'stop_words/known_words_{language}.txt', f'stop_words/backups/known_words_{language}_backup.txt')
        except:
            print(f'Creating known_words_{language}.txt')
        with open(f'stop_words/known_words_{language}.txt', 'w', encoding='utf-8') as f:
            for word in known_words:
                f.write(f'{word}\n')
        print(known_words)
        print(f'{add_words_str} {'has' if len(add_words) == 1 else 'have'} successfully been added to known_words_{language}.txt')
    elif choice == 'exit':
        exit()
