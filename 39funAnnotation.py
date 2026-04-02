x=3
y=5
def myFun(a: 'some value from funcall',b: 'some value from funcall')->'b+multiply by max(x,y) times':
    """doc...will return multiply by of max"""
    return b+a*max(x,y)
data=myFun(2,3)
print(data)
print(myFun.__doc__)
print(myFun.__annotations__)