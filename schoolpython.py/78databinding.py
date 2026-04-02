class Myclass:
    def __init__(self,cat1,cat2):
        self.cat1=cat1
        self.cat2=cat2
    def mInfo(self):
        print('from info',self.cat1,self.cat2)
obj=Myclass('orange','apple')
print(obj.cat1,obj.cat2)
obj.mInfo()