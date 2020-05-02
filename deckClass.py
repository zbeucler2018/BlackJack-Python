#Zachary Beucler
#Deck Class
#This class creates a deck of cards from the playingCardClass
#the cards from the class are shuffled and then dealt randomly

from playingCardClass import*
from random import *

class deckClass:

    #for each card in the card list, assign them a suit and a face
    def __init__(self):
        self.cardList = []
        for s in ['d', 'c', 'h', 's']:
            for i in range (1,14):
                card = playingCard(i, s)
                self.cardList.append(card)

    #have the cards in the deck appear in random order
    def shuffleDeck(self):
        for c in self.cardList:
            card1 = randrange(0, 52)
            card2 = randrange(0, 52)
            self.cardList[card1], self.cardList[card2] = self.cardList[card2], self.cardList[card1]

    #deal cards from the deck and make sure they don't show up more than once
    #pop the cards that have been played out of the deck list
    def dealCard(self):
        return self.cardList.pop(0)

    #update deck list after cards have been dealt
    #the list has the cards that remain
    def cardsRemaining(self):
        return len(self.cardList)

def main():
    #give class deckClass a variable name
    deck1 = deckClass()

    #use shuffle method to randomize the cards
    deck1.shuffleDeck()
    
    print('______________________')
    
    print(deck1.dealCard())

    
    
    print('______________________')
    print(deck1.cardsRemaining())
    
if __name__ == '__main__':
    main()
