class Myclass:
    def myMethod(self):#normal method
        self.x=5
        self.y=10
obj1=Myclass()
obj2=Myclass()
obj1.myMethod()
obj2.myMethod()#swith button
print(obj1.x,obj2.y)
