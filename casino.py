# Shane Freeborn

import math, random

class User:
    def __init__(self, name, age, funds):
        self.name = name
        self.age = age
        self.funds = funds

    def deposit_funds(self, amount):
        self.funds += amount

    def withdraw_funds(self, amount):
        self.funds -= amount

    def check_balance(self):
        if self.funds > 10:
            return True
        else:
            print("Not enough money... add more!")
            return False

class Coinflip:
    
    def outcome(self):
        outcome = random.randint(1,2)
        if outcome == 1:
            result = "Heads"
        else:
            result = "Tails"
        return result

    def begin_game(self):
        opening_prompt = input("Do you want to play Coinflip? ")
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
                opening_prompt = input("Do you want to play Coinflip? ")
        return start
    
    def user_bet(self, User):
        enough_funds = User.check_balance()
        playing = self.begin_game() == 1
        if playing and enough_funds:
            bet = input("Heads or Tails? ")
            while bet[0].lower() != "h" or bet[0].lower() !="t":
                if bet[0].lower() == "h" or bet[0].lower() == "t":
                    break
                else:
                    print("Invalid Bet")
                    bet = input("Heads or Tails? ")
            wager = int(input("How much would you like to wager? $"))
            User.withdraw_funds(wager)
            result = self.outcome()
            if result[0].lower() == bet[0].lower():
                print("It was " + result + "!")
                print("You won $" + str(wager))
                User.deposit_funds(wager*2)
                print("You now have $" + str(User.funds))
                self.play_again(User)
            else:
                print("Sorry, it was " + result)
                print("You lost $" + str(wager))
                print("You now have $" + str(User.funds))
                self.play_again(User)
        elif not playing:
            print("See ya!")

    def play_again(self, User):
        again = input("Do you want to play again? ")
        if again[0].lower() == "y":
            self.user_bet(User)
        else:
            print("Returning to Main Menu")
        
class Roulette:
    pass
class Blackjack:
    pass
class Slots:
    pass

def main():
    user_dict = {}
    if len(user_dict.keys()) == 0:
        name = input("What is your name? ")
        age = int(input("How old are you? "))
        if age < 21:
            print("Must be 21 or older to gamble!")
            return None
        starting_funds = int(input("How much do you want to start with? "))
        u = User(name, age, starting_funds)
        user_dict[name] = [age, starting_funds]
        c = Coinflip()
    pick_game = input("Which game do you want to play? (type Exit to leave) ")
    while pick_game[0].lower() == "c" or pick_game[0].lower() == "b" or pick_game[0].lower() == "r" or pick_game[0].lower() == "s" or pick_game[0].lower() == "e":
        if pick_game[0].lower() == "c":
            print("Good luck to you!")
            c.user_bet(u)
            pick_game = input("Which game do you want to play? (type Exit to leave) ")
        elif pick_game[0].lower() == "b":
            pass
        elif pick_game[0].lower() == "r":
            pass
        elif pick_game[0].lower() == "s":
            pass
        else:
            print("See you again soon!")
            break
