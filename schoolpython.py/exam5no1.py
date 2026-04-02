total=0
count=0
a=int(input('Enter the number'))
if a==0:
    print('enter other nums:')
else:
    while a!=0:
        a=int(input('enter the nums'))
        total+=a
        count+=1
    average=total/count
    print(average)
