#programmer defined function
def add(a,b):#define a,b=parameter
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
first=int(input('Please enter the first number:'))
second=int(input('Please enter the second number:'))
print('adding',add(first,second))
print('substracting',sub(first,second))
print('multiplying',mul(first,second))
print('dividing',div(first,second))