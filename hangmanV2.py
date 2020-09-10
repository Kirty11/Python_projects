#***********HANGMAN VER 2.0 ************

#import random module
import random
#read the words from the file "words.txt" into a list
with open("words.txt","r") as f:
    words=f.readlines()
#select a random word from list and covert to upper case
index=random.randint(0,len(words)-1)
theWord=words[index].strip().upper() #word to be guessed

totalChance=7 #total chance
currentChance=0 #no. of chances to start with
hangman="HANGMAN"
guessedWord='_'*len(theWord) #word to be guessed
print("********WELCOME TO HANGMAN V2.0********")
while totalChance!=0: #repeat till all the chances are exhausted
    print(guessedWord)
    #get the input from user and convert to upper case since our word is in capitals
    letter=input("Guess the letter :").upper() 
    if letter in theWord: #check if letter is present in word
        for index in range(len(theWord)): #get all the index of word
            if theWord[index]==letter: #if letter at index is the letter
                #replace the blank line at that index with letter
                guessedWord=guessedWord[:index]+letter+guessedWord[index+1:]
        #check if user has guessed correct
        if guessedWord==theWord:
            print("Congratulations!!!You Won with ",totalChance," chances to spare")
            break
    else: #if the letter guessed by user was wrong
        totalChance-=1 #totalChance=totalChance-1
        currentChance+=1
        print("Wrong choice.You are now -> ",hangman[:currentChance])
        print("Chances left ",totalChance)
#when out of while since chances are exhausted
else:
    print("The word was ",theWord)
    print("You lost..all chances exhausted")
