from collections import Counter
import re

text = input('')
words = re.findall(r"\b\w+(?:'\w+)*\b", text, flags=re.UNICODE)

counts = Counter(words)

for word, count in counts.most_common():
    print(word)

print(words)