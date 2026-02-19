x = lambda a, b, c : a + b - c #can take any number of arguments, but can only have one expression.
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a / n

mytripler = myfunc(3)
print(mytripler(15))