###################################
# Juan-Taner Allerborn
# JT-Programmieren
# WW3 Schools
# Mathe
# 17.03.2022
#####################################

import random
import string
from random_words import words

def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_word(words)
    words_letter = set(word)                            # Setzt die Buchstaben in Einzelteile
    alphabet = string.ascii_uppercase                   # Alle Buchstaben (Groß)
    used_letters = set()                                # Was der User geraten hat

    while len(words_letter) > 0:
        print("Du hast diese Buchstaben bereits benutzt: ", ' '.join(used_letters)) # Buchstaben die benutzt worden
        word_list = [letter if letter in used_letters else '-' for letter in word]  # Ersetzt beim Buchstaben ein -
        print("Der zufällige Name: ", ' '.join(word_list))

        user_letter = input("Rate einen Buchstaben: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in words_letter:
                words_letter.remove(user_letter)

        elif user_letter in used_letters:
            print("Du hast diesen Buchstaben schonmal benutzt")

        else:
            print("Unbekannter Zeichen \nVersuche es normal")


    # Wenn word letter kleiner als 0

if __name__ == '__main__':
    hangman()