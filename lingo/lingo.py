from lingowords import *
import random
from colorama import init, Fore
init(autoreset=True)

def selectedWord():
    return random.choice(words)

def guessWord():
    return input(Fore.WHITE + "Raad: ")

def wordLength(guess):
    return len(guess) == 5

def checkingForColors(guessedWord, word, correctLetters):
    tempWord = ''
    newCorrectLetters = list(correctLetters)
    
    for i in range(len(guessedWord)):
        if guessedWord[i] == word[i]:
            tempWord += (Fore.GREEN + guessedWord[i])
            newCorrectLetters[i] = guessedWord[i]
        elif guessedWord[i] in word:
            tempWord += (Fore.YELLOW + guessedWord[i])
        else:
            tempWord += (Fore.RED + guessedWord[i])

    return tempWord, ''.join(newCorrectLetters)

def hasWon(correctLetters, word):
    return correctLetters == word

def guessedLetters(correctLetters, tempWord):
    newCorrectLetters = list(correctLetters)
    for i in range(1, len(tempWord)):
        if tempWord[i] == Fore.GREEN:
            newCorrectLetters[i] = tempWord[i + len(Fore.GREEN)]
    return ''.join(newCorrectLetters)


def mainGame():
    word = selectedWord()
    attempts = 5
    won = False

    correctLetters = word[0] + "____"

    print(word)

    while not won and attempts > 0:
        guessedWord = guessWord()
        if not wordLength(guessedWord):
            print("Het woord is maar 5 letters lang.")
            continue
        
        tempWord, correctLetters = checkingForColors(guessedWord, word, correctLetters)
        print(tempWord)
        print(Fore.GREEN + correctLetters)

        won = hasWon(correctLetters, word)
        attempts -= 1
        if not won:
            print(f"Nog {attempts} pogingen over!")

    if won:
        print("Gefeliciteerd je hebt het woord geraden!")
    else:
        print(f"Jammer je hebt verloren. Het woord was: {word}")

mainGame()
