from functools import partial
def myFun(x,y,z):
    x=x+11
    y=y+11
    z=z+11
    print(x,y,z)
newFun=partial(myFun,10)
newFun(111,222)
