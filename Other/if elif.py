#import random
#number = random.randint(1, 10)

#user_guess = int(input("Guess a number 1-10: "))

#if number==user_guess:
    #print('Well Done !')
#elif number!=user_guess:
    #print('Hard Luck, try again')
    
#import random

#number = random.randint(1, 10)

#guess = int(input("Enter a number between 1 and 10: "))


#if guess == number:
    #print("Correct")
    #print("Well done!")
#elif guess < number:
    #print("Hard luck!")    
    #print("Too low")
#else:
    #print("Hard luck!")    
    #print("Too high")


#import random

#number = random.randint(1, 75)

#counter = 0


#while counter < 10:

    #guess = int(input("Enter a number between 1 and 75: "))
    #if guess == number:
        #print("Correct, Well Done")
        #break 
    #elif guess < number:
        #print("Number too low")
    #else:
        #print("Number too high")

#print('Goodbye')



import random

number = random.randint(1, 75)

keepGoing  = True

while keepGoing:

    guess = input("Enter a number between 1 and 75: ")
    
    while not guess.isdigit():
       guess = input("Enter a number between 1 and 75: ")

    
    guess = int(guess)

    if guess == number:
        print("Correct")
        goAgain = input("Play again? (Yes or No): ")
        if goAgain.upper() == "No":
            keepGoing = False
        else:
           
            number = random.randint(1, 10)

    elif guess < number:
        print("Too low")

    else:
        print("Too high")

print("Goodbye")