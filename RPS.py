import random

def RockPaperScissors():
    choice = ("Rock","Paper","Scissors")
    #pScore: Person's Score, cScore: Computer's Score
    pScore=cScore=0

    while cScore<3 and pScore<3:
        cChoice = random.choice(choice)
        #pChoice = raw_input("Enter your choice: ")
        pChoice = input("Enter your choice: ")
        #Whenever you want to quit the game, just type "Exit".
        if pChoice=="Exit":
            break
        #If you do not type "Rock", "Paper", or "Scissors", the computer asks you to type them correcly!
        if pChoice!="Rock" and pChoice!="Paper" and pChoice!="Scissors":
            print("Please choose Rock,Paper, or Scissors")
        elif (cChoice=="Rock" and pChoice=="Scissors") or (cChoice=="Paper" and pChoice=="Rock") or (cChoice=="Scissors" and pChoice=="Paper"):
            cScore=cScore+1
            print("You chose ", pChoice)
            print("Computer chose ", cChoice)
            print("Your score is", pScore)
            print("Computer score is", cScore)
        elif (pChoice=="Rock" and cChoice=="Scissors") or (pChoice=="Paper" and cChoice=="Rock") or (pChoice=="Scissors" and cChoice=="Paper"):
            pScore=pScore+1
            print("You chose ", pChoice)
            print("Computer chose ", cChoice)
            print("Your score is", pScore)
            print("Computer score is", cScore)
        elif (pChoice=="Rock" and cChoice=="Rock") or (pChoice=="Paper" and cChoice=="Paper") or (pChoice=="Scissors" and cChoice=="Scissors"):
            print("You chose ", pChoice)
            print("Computer chose ", cChoice)
            print("Your score is", pScore)
            print("Computer score is", cScore)

    if cScore>pScore:
        print("Computer Win!")
    elif cScore<pScore:
        print("You Win!")
    else:
        print("Exit")

RockPaperScissors()
