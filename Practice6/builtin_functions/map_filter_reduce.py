def f(n):
    return n+1

numbers = (1, 2, 3, 4) 
result = map(f, numbers) #executes a given function to each element of an iterable
print(result)            #represents a map object
result = set(result)
print(result)

nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))   #selects elements based on the result of a function.
print(even)

from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)