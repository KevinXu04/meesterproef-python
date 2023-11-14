class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def guess():
    while True:
        word = input("Raad: ")
        if len(word) > 5 or len(word) < 5:
            print("De woord is maar 5 letters lang")
        else:
            break
    return word

def searchGreen(word, guess):
    greenLetters = []

    for letter in range(len(word)):
        if word[letter] == guess[letter]:
            greenLetters.append(word[letter])
        else:
            greenLetters.append("_")
    return greenLetters

