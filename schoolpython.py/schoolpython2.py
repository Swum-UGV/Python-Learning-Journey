a=int(input('please enter the number:'))
if 10<=a<=99:
    if a//10==a%3:
        print('yes')
    else:
        print('no')
else:
    print('the number is worng')