from functions import *
from lingowords import *
import random

word = random.choice(words)
firstletter = word[0]
lst = [firstletter, "_", "_", "_", "_"]

for letter in lst:
    print(letter, end=" ")
print()

tries = 5
print(word)

for turn in range(tries):
    guessedWord = guess()
    print(guessedWord)
    greenLst = searchGreen(word, guessedWord)
    print(greenLst)




    tries -= 1
    print("Tries remaining: " + str(tries))

print(word)
