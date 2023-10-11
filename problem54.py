import time
import collections
from enum import Enum

## High Card: Highest value card.
## One Pair: Two cards of the same value.
## Two Pairs: Two different pairs.
## Three of a Kind: Three cards of the same value.
## Straight: All cards are consecutive values.
## Flush: All cards of the same suit.
## Full House: Three of a kind and a pair.
## Four of a Kind: Four cards of the same value.
## Straight Flush: All cards are consecutive values of same suit.
## Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

Card = collections.namedtuple('Card', ['rank', 'suit'])

def makeCardFromString(string):
    rank_str = card[:-1]
    suit_str = card[-1]

    rank_index = -1
    suit_index = -1

    return        
    
    
    

class Suit(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

class Rank(Enum):
    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12

def printHand(hand):
    # hand should have 5 elements, each representing a card
    print('Hand:')
    for card in hand:
        print(card)
        

def determineHand(hand):
    # hand has 5 cards, this function will return a string indicating the kind of hand, ie. a pair, full house, etc
    # it will also return the "rank" of that hand, as well as additional data for breaking a tie, such as high value card, or highest pair, etc
    suit_counts = [0,0,0,0]
    value_counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    pair_count = 0
    trip_count = 0

    for card in hand:
        break#rank, suit = getSuitRank(card)

        #rank_counts[rank] += 1
        #suit_counts[] += 1

    # determine if there is a straight
    # determine if there is a flush
    # determine if flush is royal
    # determine if there are any 2/3/4 of a kind
    # determine if there is a full house
    return

def isPair(hand):
    return
def isHighCard(hand):
    return

start = time.time()

player1_wins = 0
player2_wins = 0

text_file = open('p054_poker.txt', 'r')
for line in text_file:
    line = line.replace('\n','')
    print(line)
    cards = line.split(' ')

    p1 = cards[0:5]
    p2 = cards[5:10]
    printHand(p1)
    printHand(p2)
    break
    

end = time.time()
print("found in " + str(end-start) + ". Answer is: " + str(player1_wins) + '.')
