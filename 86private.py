class animal:
    def __init__(self,name,colour,age,behavior):
        self.__name=name
        self.__colour=colour
        self.__age=age
        self.__behavior=behavior
class dog(animal):
    def dmodify(self,name,colour,age,behaviour):
        self.__name=name
        self.__colour=colour
        self.__age=age
        self.__behaviour=behaviour
    def dget_data(self):
        print(self.__name,self.__colour,self.__age,self.__behaviour)
obj=dog('mini','red',3,'eat')
obj.dmodify('super','white',5,'sleep')
obj.dget_data()