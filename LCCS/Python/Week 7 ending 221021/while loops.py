import random

number = random.randint(1,10)
print(number)

counter = 1


while counter <= number:
    
    print("She loves me")
    counter = counter + 1
    
    if counter <= number:
        print("She loves me not")
        counter = counter + 1
