from functools import partial
def pow(base,exponent):
    return base ** exponent
sq=partial(pow,exponent=2)
print(sq(2))
cu=partial(pow,exponent=3)
print(cu(2))
print('testing for base with 5 and expo 3', cu(base=5))