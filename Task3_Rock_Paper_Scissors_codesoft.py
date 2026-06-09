import random
print("Welcome to Rock-Paper-Scissors")
print("Instructions:")
print("Type 'rock' , 'paper' , or 'scissors' to play")
print("You will play against the computer, Scores will be tarcked.\n")
player_score = 0
computer_score = 0
while True:
    player = input("Enter your choice(rock/paper/scissors) :").lower()
    if player not in ["rock" , "paper" , "scissors"]:
        print("Invalid chioce! Please try again \n")
        continue
    computer = random.choice(["rock" , "paper" , "scissors"])
    print(f"Computer chose:{computer}")
    if player == computer:
        print("It's aa tie")
    elif(player =="rock" and computer == "scissors") or\
        (player =="paper" and computer == "rock") or\
        (player == "scissors" and computer == "paper"):
        print("Congratulations! you won this round")
        player_score += 1
    else:
        print("Computer won this round")
        computer_score += 1
    print(f"Score-> You: {player_score} | Computer: {computer_score}\n")
    play_again = input("Do you wnat to play another round? (yes/no):").lower()
    if play_again != "yes":
        print("\n Final score:")
        print(f"You: {player_score} | Computer : {computer_score}")
        print("Thanks for playing! Bye")
        break