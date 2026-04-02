class Parent:
    def own(self):
        print('We have many money')
class Child(Parent):
    def poor(self):
        print('They are clevers')
obj=Child()
obj.own()
obj.poor()
    