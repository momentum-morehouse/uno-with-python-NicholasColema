

import random

''''
Generate the UNO deck of 100 cards. 
Paramters: None (varibiles, data types,) 
Return Values: deck->list

""'''

def buildDeck():
    deck =[]
    
    colors =["Red", "Green", "Yellow", "Blue"]
    values =[0,1,2,3,4,5,6,7,8,9,"Draw Two","Skip","Reverse"]
    wilds = ["Wild","Wild Draw four"]
    for color in colors:
        for value in values: 
          cardval = "{} {}".format(color,value)
          deck.append(cardval)
          if value != 0: 
           deck.append(cardval)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    
    return deck
 
 
"""
Shuffle's a list of items passed into it 
Paramaters: deck-> list 
Return values: deck-> list 
"""
def shuffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0,99) 
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck
''''
What this function does 
Draw card function that draws a specified number of cards of the top of the deck
Paramters: numCards -> intiger 
Return Values: cardsdrawn -> list 
'''
def drawCards(numcards): 
    cardsDrawn = []
    for x in range (numcards):
         cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

'''
Show Hand Function
Print formatted list of player's hand
Paramter: player->integer, playerHand-> list
Return values: none
'''
def showhand(player,playerHand):
    print("Player{}".format(player+1))
    print("Your hand")
    print("===========")
    y = 1
    for card in playerHand: 
        print("{}) {}".format(y,card))
        y+=1 
    print("")


'''
Check if the player can play a card, or not
Paramters: color -> string,  value-> string, playerHand-> list
Return: Boolean(Yes = True, No = False)
'''

def canPlay(color, value, playerHand):  
    for card in playerHand:
        if "wild" in splitCard[]
            return True 
        elif  color in card or value in card 
            return True 
    return False 

            
unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
unoDeck = shuffleDeck(unoDeck)
discards =[]
print(unoDeck) 
    
'''
Tootie list
'''

Player = []
numPlayers = int(input("How many players"))
while numPlayers<2 or numPlayers.4
    numPlayers = int(input("Invalid. Please enter a number between 2-4. How many players? "))
for player in range(numPlayers):   
    player.append(drawCards(5))
'''
Make a vairble that tracks which players turn it is 
and which direction the game is gonig "Intial direction" "Inverse Direction"= "Reverse Card"
'''

playerTurn = 0
playerDirection = 1
playing = True 
discards.append(unoDeck.pop(0))
splitCard = discards[0]. split ("",1)
currentColor = splitCard[0]
if currentColor != "Wild":
    cardVal = splitCard[1]
else: 
    cardVal = "Random"

while playing: 
    showhand(playerTurn,players[playerTurn])
    print("Card on top of Discard pile: {}".format(discards[-1]))
    if canPlay(currentColor,cardVal,player[playerTurn]): 
        cardChoosen = int(input("Which card do you want to play? ")) 
        while not canPlay(currentColor,cardVal,[player[playerTurn][cardChoosen-1]]):
             cardChoosen = int(input("Not a usable card? Please play a card ")) 
        print("You Played {}".format(players[playerTurn][cardChoosen-1]))
        discards.append(player[playerTurn].pop(cardChoosen-1))
        if len(player)
        print("You cannot continue until you draw a card")
        player[playerTurn].extend(drawCards(1))
    playerTurn += playerDirection

    





UnoDeck = buildDeck() 



