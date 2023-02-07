import random
import string

word = []
for i in range(10):
    word.append(random.choice(string.ascii_lowercase))
print(word)

word_str = "".join((random.choice(string.printable)) for i in range(10))
print(word_str)

