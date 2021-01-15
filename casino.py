# Shane Freeborn

import math, random

class Coinflip:
    
    def outcome(self):
        outcome = random.randint(1,2)
        if outcome == 1:
            result = "Heads"
        else:
            result = "Tails"
        print(result)

    def begin_game(self):
        opening_prompt = input("Do you want to play? ")
        if opening_prompt[0].lower() == "Y".lower():
            print("yes")
        elif opening_prompt[0].lower() == "N".lower():
            print("No")
        else:
            print("Invalid input")
            opening_prompt = input("Do you want to play? ")

