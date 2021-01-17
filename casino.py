# Shane Freeborn

import math, random

class Coinflip:
    
    def outcome(self):
        outcome = random.randint(1,2)
        if outcome == 1:
            result = "Heads"
        else:
            result = "Tails"
        return result

    def begin_game(self):
        opening_prompt = input("Do you want to play? ")
        start = 0
        while opening_prompt[0].lower() != "y" or opening_prompt[0].lower() != "n":
            if opening_prompt[0].lower() == "Y".lower():
                start = 1
                break
            elif opening_prompt[0].lower() == "N".lower():
                start = 0
                break
            else:
                print("Invalid input")
                opening_prompt = input("Do you want to play? ")
        return start
    
    def user_bet(self):
        #variable for user attributes and wages
        playing = self.begin_game() == 1
        if playing:
            bet = input("Heads or Tails? ")
            while bet[0].lower() != "h" or bet[0].lower() !="t":
                if bet[0].lower() == "h" or bet[0].lower() == "t":
                    break
                else:
                    print("Invalid Bet")
                    bet = input("Heads or Tails? ")
            wager = int(input("How much would you like to wager? $"))
            result = self.outcome()
            if result[0].lower() == bet[0].lower():
                print("It was " + result + "!")
                print("You won $" + str(wager*2))
            else:
                print("Sorry, it was " + result)
                print("You lost $" + str(wager))
        elif not playing:
            print("See ya!")
            
