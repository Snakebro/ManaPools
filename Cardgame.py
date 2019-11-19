# This game is called Mana Pools. A game where you manipulate the flow of mana from wells to create favoriable mana flow
import random


def main():
    # create a random deck of cards
    deck = generateDeck()
    # Setup gameboard
    board = generateGameboard(deck)
    return


def generateDeck(cardSuite=4, cardValueMax=10):
    cards = []
    for i in range(cardSuite):
        for j in range(1, cardValueMax + 1):
            cards.append([i, j])
    random.shuffle(cards)
    return cards


def generateGameboard(deck):
    # deal out 4 wells with num of players + 4 cards each
    well1 = genWell(deck)
    well2 = genWell(deck)
    well3 = genWell(deck)
    well4 = genWell(deck)

def genWell(deck)
	well, wellNorth, wellSouth, wellWest, wellEast = []
    for i in range(4):
        well.append(deck.pop())
        # deal 4 cards around the wells to determine a well's element
    wellNorth = deck.pop()
    wellWest = deck.pop()
    wellEast = deck.pop()
    wellSouth = deck.pop()
    


main()