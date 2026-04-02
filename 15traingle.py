row=int(input('Please enter your row'))
size=row
for i in range(1,row):
    for j in range(size):
        print(end=' ')
    size=size-1
    for k in range(1,i*2):
        print('*',end='')
    print()
