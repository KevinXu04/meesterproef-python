import random

def amountOfPlayers():
    while True:
        try:
            amount = int(input("How many players? "))
            if amount > 4:
                print("Sorry you can only play with 4 players at the same time.")
            elif amount <= 1:
                print("Sorry you can only play this game with 2 or more players.")
            else:
                return amount
        except:
            print("That is not a number!")

def creatingDeck():
    defaultCards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    specialCards = ["skip", "reverse", "draw 2", "wild card", "wild draw 4 card"]
    colors = ["blue", "green", "red", "yellow"]

    tempDeck = []
    tempSpecialDeck = []

    for card in defaultCards:
        for color in colors:
            tempDeck.append(f"{color} {card}")

    for card in specialCards[:3]:
        for color in colors:
            tempSpecialDeck.append(f"{color} {card}")

    for card in range(2):
        tempSpecialDeck += (specialCards[-2:])

    deck = tempDeck + tempDeck[:-4] + tempSpecialDeck + tempSpecialDeck
    random.shuffle(deck)

    return deck
    
def handingOutCards(amount, deck):
    players = []

    for i in range(amount):
        players.append({f"Player": i+1, "Deck": []})

    for i in range(len(players)):
        for x in range(7):
            players[i]["Deck"].append(deck[0])
            del deck[0]
    
    return players, deck