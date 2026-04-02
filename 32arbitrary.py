def s(*arg):
    length=len(arg)
    total=sum(arg)
    if length==0:

        return 0
    else:
        return total/length
result=s(5,6,7)
print(result)


      