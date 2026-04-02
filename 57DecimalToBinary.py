def decToBinary(n):
    binary=[0]*n
    i=0
    while(n>0):
        binary[i]=n%2
        n=int(n/2)
        i+=1
    for x in range(i-1,-1,-1):
        print(binary[x],end='')
decimalNumber=int(input('Please enter decimal number:'))
decToBinary(decimalNumber)