class myClass:
    def __init__(self,x=0):
        print('from class')
        self.counter=x
    def __call__(self,x=1):
        print('updating value.......')
        self.counter +=x
myObj=myClass()
inObj=myClass()
print(myClass.__init__(myObj,20))
print(myClass.__call__(inObj,10))
print(myObj.counter)
print(callable(myObj))
print(inObj.counter)
print(callable(inObj))