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
        if self.funds > 1:
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
        enough_funds = User.check_balance() #check if the user has enough money to play
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
            User.withdraw_funds(wager) #take money out of the users account
            result = self.outcome() #random of Heads and Tails
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
            if not User.check_balance():
                User.deposit_funds(int(input("Add more money here ")))
                self.user_bet(User)
            else:
                self.user_bet(User)
        else:
            print("Returning to Main Menu")
        
class Roulette:
    def outcome(self):
        number = random.randint(1,36)
        
        if number % 2 == 0:
            color = "Black"
        else:
            color = "Red"
        
        result = [color, number]

        return result
    
    def begin_game(self):
        opening_prompt = input("Do you want to play Roulette? ")
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
                opening_prompt = input("Do you want to play Roulette? ")
        return start

    def user_bet(self, User):
        enough_funds = User.check_balance() #check if the user has enough money to play
        playing = self.begin_game() == 1
        if playing and enough_funds:
            result = self.outcome() #random number
            bets = []
            color_number = input("Betting Color or Numbers? ")

            if color_number[0].lower() == "n":
                for i in range(3):
                    bet_number = int(input("Pick number {} (between 0 and 36 only!): ".format(i+1)))
                    bets.append(bet_number)
                wager = int(input("How much would you like to wager? $"))
                User.withdraw_funds(wager) #take money out of the users account

                if result[1] in bets:
                    print("It was {} {}!".format(result[0], result[1]))
                    print("You won $" + str(wager))
                    User.deposit_funds(wager*2)
                    print("You now have $" + str(User.funds))
                    self.play_again(User)
                else:
                    print("Sorry, it was {} {}".format(result[0], result[1]))
                    print("You lost $" + str(wager))
                    print("You now have $" + str(User.funds))
                    self.play_again(User)
            elif color_number[0].lower() == "c":
                color = input("Red or Black? ")
                wager = int(input("How much would you like to wager? $"))
                User.withdraw_funds(wager) #take money out of the users account
                if result[0][0].lower() == color[0].lower():
                    print("It was {} {}!".format(result[0], result[1]))
                    print("You won $" + str(wager))
                    User.deposit_funds(wager*2)
                    print("You now have $" + str(User.funds))
                    self.play_again(User)
                else:
                    print("Sorry, it was {} {}".format(result[0], result[1]))
                    print("You lost $" + str(wager))
                    print("You now have $" + str(User.funds))
                    self.play_again(User)
        elif not playing:
            print("See ya!")
    
    def play_again(self, User):
        again = input("Do you want to play again? ")
        if again[0].lower() == "y":
            if not User.check_balance():
                User.deposit_funds(int(input("Add more money here ")))
                self.user_bet(User)
            else:
                self.user_bet(User)
        else:
            print("Returning to Main Menu")

class Blackjack:

    def begin_game(self):
        opening_prompt = input("Do you want to play Blackjack? ")
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
                opening_prompt = input("Do you want to play Blackjack? ")
        return start

    def user_bet(self, User):
        enough_funds = User.check_balance() #check if the user has enough money to play
        playing = self.begin_game() == 1
        if playing and enough_funds:
            player_hand = []
            dealer_hand = []
            wager = int(input("How much would you like to wager? $"))
            for i in range(0, 2):
                player_hand.append(random.randint(1,11))
                dealer_hand.append(random.randint(1,11))
            
            print("You have " + str(player_hand[0]) + " " + str(player_hand[1]))

            while sum(player_hand) < 21:
                if sum(player_hand) > 21:
                    print("Player Bust")
                    print("Dealer Wins!")
                    return None
                elif sum(player_hand) == 21:
                    print("Player Blackjack")
                    break
                    return None

                hit_stand = input("Hit or Stand ")
                if hit_stand[0].lower() == "h":
                    player_hand.append(random.randint(1,11))
                    print("You got a " + str(player_hand[-1]))
                    print("You now have " + str(sum(player_hand)))                    
                else:
                    break
            while sum(dealer_hand) < 17:
                if sum(dealer_hand) > 21:
                    print("Player won!")
                    return None
                elif sum(dealer_hand) == 21:
                    print("Dealer Blackjack")
                    return None
                else:
                    dealer_hand.append(random.randint(1,11))

            print("Player: {} Dealer: {}".format(sum(player_hand), sum(dealer_hand)))
            if (sum(player_hand) > sum(dealer_hand) and sum(player_hand) < 22) or (sum(player_hand) <= 21 and sum(dealer_hand) < sum(player_hand)) or sum(dealer_hand) > 22 :
                print("Player won!")
                print("You won $" + str(wager))
                User.deposit_funds(wager*2)
                print("You now have $" + str(User.funds))
            elif sum(player_hand) == sum(dealer_hand):
                print("Push, try again")
            else:
                print("Dealer Won!")
                print("You lost $" + str(wager))
                User.withdraw_funds(wager)
                print("You now have $" + str(User.funds))

            self.play_again(User)

        elif not playing:
            print("See ya!")
    
    
    
    def play_again(self, User):
        again = input("Do you want to play again? ")
        if again[0].lower() == "y":
            if not User.check_balance():
                User.deposit_funds(int(input("Add more money here ")))
                self.user_bet(User)
            else:
                self.user_bet(User)
        else:
            print("Returning to Main Menu")

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
        r = Roulette()
        b = Blackjack()
    pick_game = input("Which game do you want to play? (type Exit to leave) ")
    while pick_game[0].lower() == "c" or pick_game[0].lower() == "b" or pick_game[0].lower() == "r" or pick_game[0].lower() == "s" or pick_game[0].lower() == "e":
        if pick_game[0].lower() == "c":
            print("Good luck to you!")
            c.user_bet(u)
            pick_game = input("Which game do you want to play? (type Exit to leave) ")
        elif pick_game[0].lower() == "b":
            b.user_bet(u)
            pick_game = input("Which game do you want to play? (type Exit to leave) ")
        elif pick_game[0].lower() == "r":
            r.user_bet(u)
            pick_game = input("Which game do you want to play? (type Exit to leave) ")
        elif pick_game[0].lower() == "s":
            pass
        else:
            print("See you again soon!")
            break