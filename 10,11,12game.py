import secrets
secureNumber=secrets.SystemRandom()
while True:
    print('Welcome to our game')
    press1=int(input('Press 1 to read rule or press 2 to play game'))
    if press1==1:
        print('Age must be more than 18:')
        print('Show money more than 500')
        print('You must use more than 1000 each time')
    if press1==2:
        uName=input('Press enter your name:')
        uAge=int(input('Please enter your age'))

        while len(uName)>2 and uAge>17:
            print('You can play game now')
            print('Welcome :>',uName)
            while True:
                sMoney=int(input('Please enter your show money:'))
                while sMoney>4999:
                    print('This is your money $',sMoney)
                    inputMoney=int(input('Please enter money to play'))
                    luckyNumber=int(input('Please enter your lucky number'))
                    systemNumber=secureNumber.randint(10,99)
                    while luckyNumber==systemNumber:
                        print('You are win')