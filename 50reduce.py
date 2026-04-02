import functools
list = [1,2,3,4,5,6]
print('the sum of all elements from list :', end='')
print((functools.reduce(lambda a,b: a+b,list)))