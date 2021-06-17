import random


def playGame(comp_choice):
    choices = ["Rock", "Paper", "Scissors"]

    computer = comp_choice

    player = False

    cpu_score = 0

    player_score = 0
    
    # player = input("Rock, Paper, or Scissors?").capitalize()

    player = random.choice(choices)

    if player == computer:
        print("Tie!")
        return False

    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!", computer, "covers", player)
            cpu_score += 1
            return True
        else:
            print("You Win!", player, "smashes", computer)
            player_score += 1
            return False

    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!", computer, "cut", player )
            cpu_score += 1
            return True
        else:
            print("You Win!", player, "covers", computer)
            player_score += 1
            return False

    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!", computer, "smashes", player)
            cpu_score += 1
            return True
        else:
            print("You Win!", player, "cuts", computer)
            player_score += 1
            return False

    elif player == "End":
        print("Final Scores:")
        print(f"Cpu: {cpu_score}")
        print(f"Player: {player_score}")
    

playGame("Scissors")