from random import choice

options = ["rock", "paper", "scissors"]
bot = choice(options)

ask = input("Lets play a game?: ").lower()

while ask != "no":
    game = input("rock, paper, scissors...")
    if game  == options:
        print("tie")
    elif game == "rock" and options == "scissors":
        print("You won!")    

