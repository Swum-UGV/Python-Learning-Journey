from functools import wraps
def log(fn):
    @wraps(fn)
    def with_log(*args,**kwargs):
        print(fn.__name__+" was called")
        return fn(*args,**kwargs)
    return with_log
@log
def myFun(x):
    """some operation just like arith"""
    return x
@log
def myFun2(x):
    """from my Fun 2"""
    return x
myFun(5)
print(myFun.__name__)
print(myFun.__doc__)
myFun2(3)
print(myFun2.__name__)
print(myFun2.__doc__)