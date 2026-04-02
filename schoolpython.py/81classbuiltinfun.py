#class built in function
#getattr(obj,name)
#setattr(obj,name,value)
#delattr(obj,name)
#hasattr(obj,name) True False
class Student:
    def __init__(self,name, id, age):
        self.name=name
        self.id=id
        self.age=age
sobj=Student('Swum',156,26)
print(getattr(sobj,'name'))
setattr(sobj,'age',23)
print(getattr(sobj,'age'))
delattr(sobj,'age')
print(hasattr(sobj,'age'))