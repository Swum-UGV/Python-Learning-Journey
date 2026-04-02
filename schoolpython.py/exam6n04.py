a=input('enters something')
b=''.join(a.lower().split())
c=b[::-1]
if b==c:
    print('yes')
else:
    print('no')