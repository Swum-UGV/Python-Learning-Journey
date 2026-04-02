def myFun(n):
    def adding(data):
        return data+n
    return adding
add=myFun(10)
print(add.__closure__[0].cell_contents)