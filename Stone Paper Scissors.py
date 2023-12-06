from random import *
import time

def computerChance():
    options = ["Stone" , "Paper" , "Scissors"]
    return choice(options)

def Game(user , comp , uScore , cScore):

    if (comp == "Stone"):
        if (user.upper() == "PAPER"):
            uScore += 1
            return [f"{userName} Won the Round..!!" , uScore , cScore]
        elif (user.upper() == "SCISSORS"):
            cScore += 1
            return [f"{userName} Lose the Round..!!" , uScore , cScore]
        else:
            return [" Game Tied..!!" , uScore , cScore]

    elif (comp == "Paper"):
        if (user.upper() == "SCISSORS"):
            uScore += 1
            return [f"{userName} Won the Round..!!" , uScore , cScore]
        elif (user.upper() == "STONE"):
            cScore += 1 
            return [f"{userName} Lose the Round..!!" , uScore , cScore]
        else:
            return [" Game Tied..!!" , uScore , cScore]

    elif (comp == "Scissors"):
        if (user.upper() == "STONE"):
            uScore += 1
            return [f"{userName} Won the Round..!!" , uScore , cScore]
        elif (user.upper() == "PAPER"):
            cScore += 1
            return [f"{userName} Lose the Round..!!" , uScore , cScore]
        else:
            return [" Game Tied..!!" , uScore , cScore]
    
def checkWinner(uScore , cScore):
    if (uScore > cScore):
        print(f"\nUser Score : {uScore}")
        print(f"Computer Score : {cScore}")
        print(f"\n{userName} Won the Game....!!!!")

    elif (cScore > uScore):
        print(f"\nUser Score : {uScore}")
        print(f"Computer Score : {cScore}")
        print(f"\nComputer Won the Game....!!!!")

    else :
        print(f"\nUser Score : {uScore}")
        print(f"Computer Score : {cScore}")
        print("\nGame Tied....!!!!")    
        

userName = input("Enter Your Name : ")

print(f'''\nHello {userName},
Welcome to the Game, Stone Paper Scissors. 
5 rounds will be played between you and computer in 1 Game.
Win = +1   Lose = +0   Tie = +0''')

compScore = 0
userScore = 0
round = 1


while round <= 5:

    print(f"\n-------- ROUND {round} --------")

    compChoice = computerChance()

    print("Options = Stone ; Paper ; Scissors")

    userchoice = input("Enter Your Choice : ")
    # print(userchoice.upper())
    if (userchoice.upper() not in ["STONE" , "PAPER" , "SCISSORS"]):
        print("\nWrong Choice..!!!")
        time.sleep(1.5)
        continue

    print("\nComputer Choice = ",compChoice)
    print("User Choice = ",userchoice)

    result , userScore , compScore = Game(userchoice , compChoice , userScore , compScore)

    print("\n" , result)

    round += 1

    time.sleep(2)

checkWinner(userScore , compScore)
