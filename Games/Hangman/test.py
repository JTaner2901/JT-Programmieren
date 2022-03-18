###################################
# Juan-Taner Allerborn
# JT-Programmieren
# Games
# test
# 17.03.2022
#####################################

import random
import string

from random_words import words

word = random.choice(words)
print(word)
words_letter = set(word)
print(words_letter)
alphabet = string.ascii_uppercase
print(alphabet)
used_letters = set()
print(used_letters)

print("Der Gordon".join("Der"))