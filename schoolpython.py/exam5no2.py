a=int(input('enter the first num:'))
b=int(input('enter the second num:'))
if a<b:
    for i in range(a,b+1):
        print(i,end=' ')
else:
    for i in range(a,b-1,-1):
        print(i,end='')