#Zachary Beucler
#Black Jack Class
#This class sets the rules for the actual game of Black Jack
#uses programs from all the other classes in order to work

from graphics import *
from random import *
from deckClass import *
from BlackJackClass import *
from buttonClass import *
from playingCardClass import *


"""Attributes of this Blackjack class are as follows.
       INSTANCE VARIABLES

        dealerHand: a list of PlayingCard objects representing the dealer's hand
        playerHand: a list of PlayingCard objects representing the player's hand
        playingDeck: a Deck object representing the deck of cards the game is being played with
        
       METHODS
       
        __init__(self, dHand=[], pHand=[])
            constructor that initializes instance variables
            it also gives the playingDeck an initial shuffle
        initDeal(self,gwin,xposD,yposD,xposP,yposP):
            deals out initial cards, 2 per player and 
            displays dealer and player hands on graphical win
            xposD and yposD give initial position for dealer cards
            xposP and yposP are analogous
        hit(self, gwin, xPos, yPos)
            adds a new card to the player's hand and places it at xPos, yPos
        evaluateHand(self, hand)
            totals the cards in the hand that is passed in and returns total
            (ace counts as 11 if doing so allows total to stay under 21)
        dealearPlays(self, gwin, xPos, yPos)
            dealer deals cards to herself, stopping when hitting "soft 17"
"""

class BlackJackClass:
    #assigns cards to the player's hand and the dealer's hand
    #also shuffles the deck of cards from the deck class
    def __init__(self, dHand=[], pHand=[]):
        self.dHand = dHand
        self.pHand = pHand
        self.deck = deckClass()
        self.deck.shuffleDeck()

    #first deal of cards to start the game
    def initDeal(self, gwin, xposD, yposD, xposP, yposP):
        for i in range(4):
            #gives 2 cards to the player and 2 cards to the dealer for initial hand
            if i == 0 or i == 2:
                self.dHand.append(self.deck.dealCard())
            else:
                self.pHand.append(self.deck.dealCard())
                
        print(self.pHand)

        for i in range(0, 2):
            #get dealer suit
            dSuit = self.dHand[i].getSuit()
            #get dealer card
            dCard = self.dHand[i].getRank()

            #get player suit
            pSuit = self.pHand[i].getSuit()
            #get player card
            pCard = self.pHand[i].getRank()

            #draw dealer cards
            dealFirst = Image(Point(xposD, yposD), "playingcards/" + str(dSuit) + str(dCard) + ".gif") 
            #draw player hand
            playFirst = Image(Point(xposP, yposP), "playingcards/" + str(pSuit) + str(pCard) + ".gif")

            #draws the cards for each player on the screen
            dealFirst.draw(gwin)
            playFirst.draw(gwin)

            #positions the cards on the screen to overlap, but still look nice
            xposD += 20
            xposP += 20

        #return the dealer hand, player hand
        return self.dHand, self.pHand
            
    #allow for player to add more cards to their hands in order to get closer to 21
    #takes cards from the deck and keeps dealing every time Hit is clicked in main function
    def hit(self, gwin, xPos, yPos):
        dcard= self.deck.dealCard()
        dealSuit= dcard.getSuit()
        dealCard= dcard.getRank()

        #draws the card images in the window              
        dealDraw = Image(Point(xPos+20*len(self.pHand), yPos), "playingcards/" + str(dealSuit) + str(dealCard) + ".gif")
        dealDraw.draw(gwin)
            

        #appends player's cards in hand 
        self.pHand.append(dcard)
        return self.pHand
                
                              
            
    #takes the number of cards in hand and each of their values and adds the values together
    #with evaluated number, program can figure out what your score is
    #and whether or not you are under 21 or over
    def evaluateHand(self, hand):
        total = 0
        hasAce = False
        
        for i in hand:
            #gets the rnk of each card in the window
            card = i.getRank()
            #evaluates each of the card values
            if card > 10:
                card = 10
            if card == 1:
                hasAce = True
                card = 11
            total= total+card
        #evaluates if card total is over 21 but there is an Ace
        #Ace can either have a value of 1 or 11
        if total > 21 and hasAce:
            total = total -10
            hasAce = False
        if total > 21:
            return total #means busted
        else:
            return total

    #dealer (opponents) turn to try and get to 21           
    def dealerPlays(self, gwin, xPos, yPos):
        dHand= self.evaluateHand(self.dHand)
        #dealer can not have a hand under than 17
        #cards from dealer's deck become appended from deck after shown on screen
        while dHand < 17:
            dcard= self.deck.dealCard()
            self.dHand.append(dcard)
            #same evaluation function as for player
            dHand = self.evaluateHand(self.dHand)
            
        
        for i in self.dHand:
            #allow for player to add more cards to their hands in order to get closer to 21
            #takes cards from the deck and keeps dealing every time Hit is clicked in main function
            dSuit= i.getSuit()
            dCard= i.getRank()
            dealSecond= Image(Point(xPos, yPos), "playingcards/" + str(dSuit) + str(dCard) + ".gif")
            dealSecond.draw(gwin)
            xPos += 20
            
                 
        return self.dHand
        

if __name__ == '__main__':
    main()

    
    

    
