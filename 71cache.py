def memorize(fibo):
    cache=dict()
    def inner(n):
        if n not in cache:
          cache[n]=fibo(n)
        return cache[n]
    return inner
@memorize
def fact(n):
    print('Calculating the fact {0}'.format(n))
    return 1 if n<2 else n*fact(n-1)
print(fact(6))
print(fact(8))