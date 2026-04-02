def myFun(x,y):
    return x+y
myFun.__subject__='bio'
myFun.__mark__=90
print(dir(myFun))
print(myFun.__subject__) 