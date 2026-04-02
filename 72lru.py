from functools import lru_cache
@lru_cache(maxsize=3)
def fib(n):
    print('Calculating fib{0}'.format(n))
    return 1 if n<3 else fib(n-1)+fib(n-2)
print(fib(6))
print(fib(3))