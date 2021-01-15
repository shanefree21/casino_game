# Shane Freeborn

import math, random

class Coinflip:

    def __init__(self, head, tails):
        self.head = head
        self.tails = tails
    
    def outcome(self):
        outcome = random.randint(1,2)
        if outcome == 1:
            result = "Heads"
        else:
            result = "Tails"

    def begin_game(self):
        opening_prompt = input("Do you want to play? ")
        if opening_prompt[0] = "Y".lower():
            print("yes")
        elif opening_prompt[0] = "N".lower():
            print("No")
