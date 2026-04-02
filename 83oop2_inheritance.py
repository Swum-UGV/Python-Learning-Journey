class Base1:
    def multi(self,a,b):
        return a*b
class Base2(Base1):
    def Adding(self,a,b):
        return a+b
class Derived(Base2):
    def Sub(self,a,b):
        return a-b
obj=Derived()
print('from Base1 ',obj.multi(5,5))
print('from Base2 ',obj.Adding(5,6))
print('from Base3 ',obj.Sub(3,4))