num=[]
while True:
    user=int(input('enter the nums:'))
    if user==0:
        break
    else:
     num.append(user)
num.sort()
print(num)