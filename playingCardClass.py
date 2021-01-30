# Zachary Beucler
# Playing Card Class
# This class creates playing cards that will appear in the main function of Black Jack

class playingCard:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # give each of the cards in the deck a ranking as to how much each card is worth
    def getRank(self):
        return self.rank

    # assign each card one of the four suits, either diamonds, clubs, spades, hearts
    def getSuit(self):
        return self.suit

    # place value for the cards based on their ranks from above
    def Value(self):
        if self.rank > 10:
            return 10
        else:
            return self.rank

    # defines what rank and suitColor is for each card
    # gives each card in the deck a value/rank and a suit color
    def __str__(self):
        rank = ["Ace", "Two", "Three", "Four", "Five", "Six",
                "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        suitColor = {'d': 'Diamonds', 'c': 'Clubs',
                     's': 'Spades', 'h': 'Hearts'}
        rankName = rank[self.rank]
        suitName = suitColor[self.suit]
        card = rankName + ' of ' + suitName
        return card


if __name__ == '__main__':
    main()
