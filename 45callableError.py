class myClass:
    def __init__(self,x=0):#constructor
        print('from class')#constructor
        self.counter=x#constructor
    def __call__(self,x=11):#callable object
        print('updating value......')#callable object
        self.counter +=x #callable object
    def myFun(self, z=1):#normal method
        print('from myFun new........')#normal method
        self.counter +=z#normal method
myObj=myClass()#Object creation
inObj=myClass()#Object creation
myFunobj=myClass()#Object creation
print(myClass.__init__(myObj,20))
print(myClass.__call__(inObj,10))
print(myClass.myFun(myFunobj,30))
print(myObj.counter)#State check
print(callable(myObj))#State check
print(inObj.counter)#State check
print(callable(inObj))#State check

print(callable(myFunobj.myFun))#method callable check
myObj()#object ko function lo khaw tar
print(myObj.counter)
inObj()
print(inObj.counter)

print('my myfunobj value is ',myFunobj.counter)
myFunobj()
print('after calling')
print(myFunobj.counter)