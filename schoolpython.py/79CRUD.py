class Myclass:
    def __init__(self):
        self.name='sai'
        self.age='25'
        self.hobby='lazy'
    def update(self):
        self.name='swum'
        self.age='26'
        self.hobby='programming'
o1=Myclass()
o2=Myclass()
print('Before upadting.....')
print(o1.name,o1.age,o1.hobby)
print(o2.name,o2.age,o2.hobby)
o1.update()
o2.update()
print('After updating........')
print(o1.name,o1.age,o1.hobby)
print(o2.name,o2.age,o2.hobby)