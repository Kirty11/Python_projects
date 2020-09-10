import random

roundNo=1 #intialize

#declare variables for maintaining score
myScore=0 #keeps track of my score
cScore=0 #keeps track of computer score
tie=0 #keeps track of no. of ties

#Play the game for 10 rounds
while roundNo<=10:
    #print the round no
    print()
    print("ROUND : ",roundNo)    

    #get user choice, from the choices available
    print("1 Rock")
    print("2 Paper")
    print("3 Scissor")
    myChoice=int(input("Enter your choice(1-3)"))

    #get computer choice
    cChoice=random.randint(1,3)
    print("Computer chose :",cChoice)

    #update score
    if myChoice==cChoice:
        tie+=1
        print("Tie")
    elif myChoice==1 and cChoice==3:
        myScore+=1
        print("You scores")
    elif myChoice==2 and cChoice==1:
        myScore+=1
        print("You scores")
    elif myChoice==3 and cChoice==2:
        myScore+=1
        print("You scores")
    elif cChoice==1 and myChoice==3:
        cScore+=1
        print("Computer scores")
    elif cChoice==2 and myChoice==1:
        cScore+=1
        print("Computer scores")
    elif cChoice==3 and myChoice==2:
        cScore+=1
        print("Computer scores")


    #print current score tally
    print("Your Score :",myScore)
    print("Computer Score :",cScore)
    print("Tied :",tie)

    #increment the current round
    roundNo+=1

#compute the winner
print()
if myScore>cScore:
    print("Congratulations!! you won")
elif cScore>myScore:
    print("Computer won..try again")
else:
    print("Game ends in a tie")

    
    

    

