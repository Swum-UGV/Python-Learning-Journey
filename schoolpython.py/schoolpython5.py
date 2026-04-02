from random import randint
x=randint(1,25)
choice=0
while choice<5:
    print('Enter the number from 1 to 25')
    guess=int(input('Enter your guess number:'))
    choice+=1
    if guess>x:
        print('Your number is bigger than x')
    elif guess<x:
        print('Your number is smaller than x')
    else:
        break
if guess == x:
    print('Your are right in'+str(choice)+' times ')
else:
    print('You are worng! My number is'+str(x))