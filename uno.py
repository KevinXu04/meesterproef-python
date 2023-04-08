from functions import *

amount = amountOfPlayers()

deck = creatingDeck()

players, deck = handingOutCards(amount, deck)

print(players, len(deck))

