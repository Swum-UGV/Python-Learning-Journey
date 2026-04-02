work=[]
while True:
    user=input('enter work what you want:')
    if user=='stop':
        break
    if user in work:
        print('Already!')
    else:
        work.append(user)
print(work)
