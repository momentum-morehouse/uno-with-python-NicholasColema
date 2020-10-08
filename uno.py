NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS =["🔴","🔵" ]




class Card:
    def __init__(self, NUMBERS, COLORS): 
        self.number = number
        self.color = color
    
    def __str__(self):
        return f"{self.color,}{self.number}"
        

class Player: 
    def __init__(self, name):
        self.name = name 



class Deck: 
    def __init__(self, name):
        self.cards = []
        for number in numbers: 
            for color in colors: 
                card = (color, number)
                self.cards.append(card)
        

class Game: 
    pass 

