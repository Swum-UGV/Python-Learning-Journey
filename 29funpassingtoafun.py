def square(a):
    return a**2
def cube(b):
    return b**3
def funtofun(fun,n):
    return fun(n)
a=funtofun(cube,3)
b=funtofun(square,10)
print('calling cube function:',a)
print('calling square function:',b)