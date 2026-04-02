def binaryToDec(b):
    num=b
    dec=0
    base=1
    temp=num
    while(temp):
        digit=temp%10
        temp=int(temp/10)
        dec+=digit*base
        base=base*2
    return dec
bnumber=1010
print(binaryToDec(bnumber))