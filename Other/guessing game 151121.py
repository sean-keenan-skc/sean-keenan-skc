import random

number = random.randint(1,10)


counter = 0

while counter < 3:
    
    guess = int(input('Enter a number between 1 and 10:'))
    if guess == number:
        print('Correct')
        break
    elif guess < number:
        print('Too low')
    else:
        print('Too high')
        
    counter = counter + 1
    
print('Goodbye')