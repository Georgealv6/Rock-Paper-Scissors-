from random import choice

ask = input("Lets play a game?: ").lower()

while ask != "no":
    options = ["rock", "paper", "scissors"]
    bot = choice(options)
    game = input("rock, paper, scissors...").lower()
    if game == bot:
        print("tie")
    elif game == "rock" and bot == "scissors":
        print("They chose..", bot,"You won!")    
    elif game == "scissors" and bot == "rock":
        print("They chose..", bot,"You lose!")  
    elif game == "scissors" and bot == "paper":
        print("They chose..", bot,"You won!")    
    elif game == "paper" and bot == "scissors":
        print("They chose..", bot,"You lose!")    
    elif game == "paper" and bot == "rock":
        print("They chose..", bot,"You won!")    
    elif game == "rock" and bot == "paper":
        print("They chose..", bot,"You lose!")    
    else:
        print("shoot!")
    ask = input("Lets play a game?: ").lower()
