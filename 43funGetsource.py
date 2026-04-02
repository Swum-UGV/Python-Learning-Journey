import inspect
from inspect import isfunction,ismethod
import math
def myFun(x,y,z=10,*,kw1,kw2=2):
    return x+y
print(myFun.__name__)#name
print(myFun.__defaults__)#positional arguments
print(myFun.__kwdefaults__)#keyword only arguments
print(myFun.__code__.co_varnames)
print(myFun.__code__.co_argcount)
print(inspect.getsource(myFun))
print('checking is function ',isfunction(myFun))
print('checking is method ',ismethod(myFun))
print(inspect.getmodule(print))
print(inspect.getmodule(ismethod))
print(inspect.getmodule(math.sin))