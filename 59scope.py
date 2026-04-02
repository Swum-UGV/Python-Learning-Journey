def outerFun():
    d='green'
    def innerFun1():
        def innerFun2():
            print('the most inner2',d)
        innerFun2()
        nonlocal d
        d='python'
        print('the second inner',d)
    innerFun1()
    print('the outer fun',d)
outerFun()
        