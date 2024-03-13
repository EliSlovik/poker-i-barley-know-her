import random
from CalcStren import CalcStren

undealtCards = [
    "Ace of Spades", "King of Spades", "Queen of Spades", "Jack of spades",
    "Ten of Spades", "Nine of Spades", "Eight of Spades", "Seven of Spades",
    "Six of Spades", "Five of Spades", "Four of Spades", "Three of Spades",
    "Two of Spades", "Ace of Hearts", "King of hearts", "Queen of Hearts",
    "Jack of Hearts", "Ten of Hearts", "Nine of Hearts", "Eight of Hearts",
    "Seven of Hearts", "Six of Hearts", "Five of Hearts", "Four of Hearts",
    "Three of Hearts", "Two of Hearts", "Ace of Clubs", "King of Clubs",
    "queen of clubs", "Jack of Clubs", "Ten of Clubs", "Nine of Clubs",
    "Eight of Clubs", "Seven of Clubs", "Six of Clubs", "Five of Clubs",
    "Four of Clubs", "Three of Clubs", "Two of Clubs", "Ace of Diamonds",
    "King of Diamonds", "Queen of Diamonds", "Jack of Diamonds",
    "Ten of Diamonds", "Nine of Diamonds", "Eight of Diamonds",
    "Seven of Diamonds", "Six of Diamonds", "Five of Diamonds",
    "Four of Diamonds", "Three of Diamonds", "two of Diamonds", "Hypatia of alexandria", "John of Cena" ]

#print(undealtCards)
bankAM = 1000
x = 0
# heartCount = 0
# spadeCount = 0
# clubCount = 0
# diamondCount = 0
calcStren = CalcStren()
def dealCard():
  global x
  if x < len(undealtCards):
    dealtCard = undealtCards[x]
    x += 1
    return dealtCard
  else:  
    print("there are no more cards")
  
def shuffleDeck():
  random.shuffle(undealtCards)
  x = 0


shuffleDeck()
# bet_amount = int(input("How much would you like to bet? "))
# bankAM = bankAM - bet_amount


playerCards = [dealCard() for _ in range(2)]
dealerCards = [dealCard() for _ in range(2)]
communityCards = [dealCard() for _ in range(5)]

print(playerCards)
print(dealerCards)
print(communityCards)

playerSuits = calcStren.calcSuit(*playerCards, *communityCards)
dealerSuits = calcStren.calcSuit(*dealerCards, *communityCards)

def check_flush(suits):
  for suit, count in suits.items():
      if count >= 5:
          return True
  return False

# check for player flush
if check_flush(playerSuits):
  print(
    "The player has a flush!")
else:
  print("The player does not have a flush.")

# check for dealer flush
if check_flush(dealerSuits):
  print("The dealer has a flush!")
else:
  print("The dealer does not have a flush.")

