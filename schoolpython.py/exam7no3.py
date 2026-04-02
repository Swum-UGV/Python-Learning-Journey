neg=[]
pos=[]
zero=[]
while True:
    user=input('Enter the nums:')
    if user=='':
        break
    num=int(user)
    if num<0:
        neg.append(user)
    elif num==0:
        zero.append(user)
    else:
        pos.append(user)
print(neg,pos,zero,sep='\n')
