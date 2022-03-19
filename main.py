import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Choose, rock, paper or scissors?: ")

    print("Player: ", player)
    print("Computer: ", computer)

    if player == computer:
        print("It's a Tie")
    if player == "rock" and computer == "paper":
        print("You Lose!")
    if player == "rock" and computer == "scissors":
        print("You Win!")
    if player == "paper" and computer == "rock":
        print("You Win!")
    if player == "paper" and computer == "scissors":
        print("You Lose!")
    if player == "scissors" and computer == "rock":
        print("You Lose!")
    if player == "scissors" and computer == "paper":
        print("You Win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye! buddy")