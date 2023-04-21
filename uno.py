from functions import *

amount = amountOfPlayers()

deck = creatingDeck()

players, deck = handingOutCards(amount, deck)

deck, discardPile = piles(deck)

turns(players, deck, discardPile)

print(players, len(deck), discardPile)