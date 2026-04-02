def myFun():
    data='data is belong to myFun'
    def inner():
        print(data)
    return inner
obj= myFun()
del myFun
obj()