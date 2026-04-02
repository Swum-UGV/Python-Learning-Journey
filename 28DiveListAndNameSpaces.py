a=20
def outfun():
    print(a)
    a=20
    def innerfun():
        print(a)
        a=30