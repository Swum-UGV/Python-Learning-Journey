num=1
for row in range(5):
    for col in range(5):
        if (row+col)%2==0:
            print(f'*',end=' ')
        else:
            print(num,end=' ')
            num+=1
    print()