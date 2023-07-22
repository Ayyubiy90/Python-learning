from random import randint


player1 = input("player 1, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else: 
    computer = "scissors"
print(f"Ccomputer plays {computer}" )


# computer = player2
player2 = computer

if player1 == player2:
    print("it's a tie")
elif player1 == "rock":
    if player2  == "scissors":
        print("player1 wins!")
    elif player2 == "paper":
        print("computer wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins!")
    elif player2 == "scissors":
        print("computer wins!")
elif player1 == "scissors":
    if player2 == "rock":
        print("computer wins!")
    elif player2 == "paper":
        print("computer wins!")
else: 
    print("something is wrong")
