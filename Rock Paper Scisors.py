from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False
scores=[0,0]
print (scores)
while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            scores[1]+=1
        else:
            print("You win!", player, "smashes", computer)
            scores[0]+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            scores[1]+=1
        else:
            print("You win!", player, "covers", computer)
            scores[0]+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)

            scores[1]+=1
        else:
            print("You win!", player, "cut", computer)
            scores[0]+=1
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False

    if scores[0] == 2:
        print ("Game Over, you win")
        player = True
    if scores[1] == 2:
        print ("Game Over, computer win")
        player = True

    computer = t[randint(0,2)]




