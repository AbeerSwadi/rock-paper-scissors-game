import random

print("Game Rules ")
trying = 0
while trying < 6:
    player = input("choose one of this (Rock ,paper, scissors)  ")

    Word = ["rock", "paper", "scissors"]
    cpu_choose = random.choice(Word)
    print(" your choose is: " + player)
    print("computer choose is :" + cpu_choose)
    if (
        player == "rock"
        and cpu_choose == "scissors"
        or player == "paper"
        and cpu_choose == "rock"
        or player == "scissors"
        and cpu_choose == "paper"
    ):
        print("Congratulations , You won ")
        print(20 * "_")
    elif (
        player == "rock"
        and cpu_choose == "rock"
        or player == "paper"
        and cpu_choose == "paper"
        or player == "scissors"
        and cpu_choose == "scissors"
    ):
        print(" the same choose ")
        print(20 * "_")

    else:
        print(" You lose ,try agine ")
        print(20 * "_")

    trying += 1
