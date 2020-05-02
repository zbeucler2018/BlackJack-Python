#Zachary Beucler
#Program Assignment 5: Black Jack
#COM 110
#This program will allow for the user to play a game of Black Jack against a
#computer generated dealer

from graphics import *
from time import *
from random import *
from deckClass import *
from BlackJackClass import *
from buttonClass import *
from playingCardClass import *


        
def main():
    #open graphics window 
    win = GraphWin("Black Jack", 600, 600)
    background = Rectangle(Point(0,0), Point(600,600))
    background.setFill("darkgreen")
    background.draw(win)

    #welcome message with instructions on how game works
    welcome = Text(Point(win.getWidth()/2, 150), "Welcome to Black Jack")
    welcome.setFill("white")
    welcome.setSize(36)
    welcome.draw(win)
    welcome1 = Text(Point(win.getWidth()/2, 225), "This is a super fun program that allows you to play Black Jack! ")
    welcome1.setFill("white")
    welcome1.setSize(14)
    welcome1.draw(win)
    welcome2 = Text(Point(win.getWidth()/2, 275), "Your opponent is the dealer who is computer generated. ")
    welcome2.setFill("white")
    welcome2.setSize(14)
    welcome2.draw(win)
    welcome3 = Text(Point(win.getWidth()/2, 325), "Press the Start button to begin, if you want another card press Hit. ") ##
    welcome3.setFill("white")
    welcome3.setSize(14)
    welcome3.draw(win)
    begin = Text(Point(win.getWidth()/2, 375), "When you are happy with your hand, press Stand. The dealer will then take his/her turn.")
    begin.setFill("white")
    begin.setSize(14)
    begin.draw(win)
    begin2 = Text(Point(win.getWidth()/2, 425), "Click anywhere to begin!!!")
    begin2.setFill("white")
    begin2.setSize(14)
    begin2.draw(win)
    win.getMouse()
    #undraw the welcome messages in order to start the program
    welcome.undraw()
    welcome1.undraw()
    welcome2.undraw()
    welcome3.undraw()
    begin.undraw()
    begin2.undraw()
    player= Text(Point(50,420), "Player:")
    player.setFill("white")
    player.setSize(20)
    player.draw(win)
    dealer= Text(Point(50, 80), "Dealer:")
    dealer.setFill("white")
    dealer.setSize(20)
    dealer.draw(win)
 
    

    #hit button and exit button
    hitBtn= Button(win, Point(250,300), 75, 50, "Hit")
    standBtn= Button(win, Point(350, 300), 75,50, "Stand")
    exitBtn= Button(win, Point(550,550), 75, 50, "Exit")
    startBtn = Button(win, Point(150, 300), 75, 50, "Start")
    
    #call BlackJackClass so that it can be reused in the main function   
    pt = win.getMouse()

    #while loop so that the game won't begin until after start button is clicked
    while not startBtn.clicked(pt):
        pt = win.getMouse()

    #once start button is clicked, the game of Black Jack begins
    game = BlackJackClass()
    #player and dealer are dealt cards
    dHand, pHand = game.initDeal(win, 200, 80, 200, 420)
    coverCard = Image(Point(220, 80), "playingcards/" + "b2fv" + ".gif")
    coverCard.draw(win)


    #after start button is clicked, the score of player will appear next to "player"
    xPos= 200
    player.setText("Player: " + str(game.evaluateHand(pHand)))

    #if exit button is not clicked, program runs based on how many times
    #the hit button is clicked
    #can continue to click hit button until stand button is pressed
    while not exitBtn.clicked(pt):
        if hitBtn.clicked(pt):
            pHand= game.hit(win,xPos, 420)
            exitBtn.activate()
            #score updates after each card is added
            player.setText("Player: " + str(game.evaluateHand(pHand)))
            
        #when stand button is clicked, dealers turn to play until they lose/stand
        elif standBtn.clicked(pt):
            dHand= game.dealerPlays(win, xPos, 80)
            coverCard.undraw()
            #if player's hand is over 21, they bust
            if game.evaluateHand(pHand) > 21:
                loser= Text(Point(win.getWidth()/2, 200),"You Lose, Busted")
                loser.setFill("white")
                loser.setSize(30)
                loser.draw(win)
            #if dealer's hand if over 21, player wins, dealer busts
            elif game.evaluateHand(dHand) > 21:
                winner= Text(Point(win.getWidth()/2, 200),"You Win, Dealer Busted!!!")
                winner.setFill("white")
                winner.setSize(30)
                winner.draw(win)
            #if dealer's hand is greater than player's but still < 21, dealer wins
            elif game.evaluateHand(pHand) < game.evaluateHand(dHand):
                loser2= Text(Point(win.getWidth()/2,200),"You Lose, Dealer Got Higher Score")
                loser2.setFill("white")
                loser2.setSize(30)
                loser2.draw(win)
            #if both dealer and player bust, it's a tie
            elif game.evaluateHand(pHand) and game.evaluateHand(dHand) > 21:
                tie = Text(Point(win.getWidth()/2, 200),"You Both Busted, Tie!")
                tie.setFill("white")
                tie.setSize(30)
                tie.draw(win)
            #if dealer and player do not bust and dealer has less than player, player wins
            else:
                winner2= Text(Point(win.getWidth()/2, 200), "You Win!!!")
                winner2.setFill("white")
                winner2.setSize(30)
                winner2.draw(win)
        
            #dealer's score is shown on screen
            #score updates after each card is added
            dealer.setText("Dealer: " + str(game.evaluateHand(dHand)))                
        
        #deactivate exit button               
        pt = win.getMouse()
    exitBtn.deactivate()
    win.close()

   
        
   
    
     
main()
        





    
