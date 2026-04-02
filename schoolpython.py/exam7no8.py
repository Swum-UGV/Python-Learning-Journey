u=[10,20,30,40,50,60]
user=int(input('enter the nums:'))
if user in u:
    u.remove(user)
else:
    u.pop(0)
    u.pop(-1)
print('u',u)
print(len(u))
