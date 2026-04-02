def myFun(n):
    def addding(data):
        return data+n
    return addding
add=myFun(10)
addd=myFun(20)
print('this will be add 10=',add(20))
print('this will be add=',addd(30))
print('this will be added=',addd(add(5)))