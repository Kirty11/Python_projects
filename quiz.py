#************riddles**************#
import random
#print the introductory message
print("Welcome to Super Coder Riddles Quiz!!!")
print('_'*30)
#initialize score and dictionary
score=0
riddles={}
#read everything from file
with open("riddles.txt","r") as f:
    questions=f.readlines()
    #get each question from the list
    #split on the basis of : as q and a
    for question in questions:
        q,a=question.strip().split(':')
        riddles[q]=a

#print the rules.
print()
print("Max questions asked :5")
print("Correct answer : 2 marks")
print("Wrong answer :-1 mark")
print()
#initialize the questions asked count
qCount=0
#get keys all keys from riddles and convert to list
questions=list(riddles.keys())
#shuffle list
random.shuffle(questions)
#read each question from list
for q in questions:
    #print question and get answer
    print(q)
    ans=input("Enter your answer :")
    #compare both answer by converting to lower case
    #update and  print score
    if ans.lower()==riddles[q].lower():
        print("Correct answer")
        score=score+2
    else:
        print("You got it wrong.Better luck next time")
        print("Correct answer :",riddles[q])
        score=score-1
    print("Score :",score)
    #increment question count and exit if 5
    qCount=qCount+1
    if qCount==5:
        break
print()
print("End of riddles quiz")
print("Total Score :",score)
    
      
            
                  
