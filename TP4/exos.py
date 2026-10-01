import random

class Product:
    def __init__(self, code:str, name:str, price:float):
        self.code = code
        self.name = name
        self.price = price
        self.tax = 0.2

    def get_price(self):
        return self.price + self.price*self.tax

p1 = Product("1223", "POMME", 36)
print(p1.get_price())

# EXO 2

class Fraction:
    def __init__(self, numérateur, dénominateur):
        self.n = numérateur
        self.d = dénominateur

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, f2):
        n = self.n * f2.d + self.d * f2.n
        d = self.d * f2.d
        return Fraction(n, d)

    def __sub__(self, f2):
        n = self.n * f2.d - self.d * f2.n
        d = self.d * f2.d
        return Fraction(n, d)

    def __mul__(self, f2):
        n = self.n * f2.n
        d = self.d * f2.d
        return Fraction(n, d)

    def __truediv__(self, f2):
        n = self.n * f2.d
        d = self.d * f2.n
        return Fraction(n, d)

    def __gt__(self, f2):
        return self.n * f2.d > f2.n * self.d

    def __lt__(self, f2):
        return self.n * f2.d < f2.n * self.d

    def __le__(self, f2):
        return self.n * f2.d <= f2.n * self.d

    def __ge__(self, f2):
        return self.n * f2.d >= f2.n * self.d

    def __eq__(self, f2):
        return self.n * f2.d == f2.n * self.d

    def __ne__(self, f2):
        return self.n * f2.d != f2.n * self.d

# Exo 3

class CardValue:
    def __init__(self, val_txt, val_pts):
        self.val_txt = val_txt
        self.val_pts = val_pts

class CardColor:
    def __init__(self, shade, shade_name, foregroud_color, backgroud_color):
        self.shade = shade
        self.name = shade_name
        self.fg = foregroud_color
        self.bg = backgroud_color

class Card:
    def __init__(self, value, color):
        self.v = value
        self.c = color

    def __gt__(self, Card2):
        return self.v.val_pts > Card2.v.val_pts

    def __lt__(self, Card2):
        return self.v.val_pts < Card2.v.val_pts

    def is_equal_value(self, Card2):
        return self.v.val_pts == Card2.v.val_pts

    def __str__(self):
        return self.v.val_txt + self.c.shade

    def __repr__(self):
        return str(self)

class Deck:
    def __init__(self):
        self.defausse = []
        self.deck = []
        self.current = None
        self.noms = ["2", "3", "4", "5", "6", "7", "8", "8", "10", "V", "Q", "K", "A"]
        self.vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.shade = ["♠","♣","♦","♥"]
        self.shade_name = ["pique", "trefle", "carreau", "coeur"]
        self.colors = ["noir", "noir", "rouge", "rouge"]

    def init52_cards(self):
        for i in range(13):
            for j in range(4):
                v = CardValue(self.noms[i], self.vals[i])
                c = CardColor(self.shade[j], self.shade_name[j], self.colors[j], "blanc")
                self.deck.append(Card(v, c))

    def shuffle(self):
        random.shuffle(self.deck)

    def Draw(self):
        self.current = self.deck[-1]
        self.deck.pop()
        return self.current
    
    def Discard(self, card):
        self.defausse.append(card)

    def __str__(self):
        if self.current != None:
                    return self.current.v.val_txt + self.current.c.shade
    
    def __repr__(self):
        return str(self)
    
# ----------- JEU ---------------

def Jeu(j, r, deck):
    if j > 9:
        return "joueur à gagné"
    if r > 9:
        return "robot à gagné"
    print("carte Actuelle :")
    current = deck.Draw()
    print(current)
    choix = input("Prochaine carte + ou - ?")
    deck.Discard(current)
    new = deck.Draw()
    print("Nouvelle carte :")
    print(new)
    print("----------------------------------------")
    if choix == '+':
        if current > new:
            print("gagné !")
            Jeu(j+1, r, deck)
        else:
            print("perdu !")
            Jeu(j, r+1, deck)    
    if choix == '-':
        if current > new:
            print("perdu !")
            Jeu(j, r+1, deck)
        else:
            print("gagné !")
            Jeu(j+1, r, deck)


deck = Deck()
deck.init52_cards()
deck.shuffle()
Jeu(0, 0, deck)