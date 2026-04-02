#class built in attribute
class Myclass:
    """This is my first professional class"""
    variable='programming'
    def active(self):
        print(f'hello from {self.variable}')
print(Myclass.__doc__)
print(Myclass.__dict__)