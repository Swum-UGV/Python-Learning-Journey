import secrets
print('Printing integer number using secrets module')
data=secrets.SystemRandom()
test=data.randrange(0,99,3)
print('Your  number is:',test)