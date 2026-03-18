names = ["Ali", "Bob", "Dana"]
 
for i, name in enumerate(names):    #adds a counter to an iterable and returns it
    print(i, name)
print(list(enumerate(names, 2)))


names = ["Ali", "Bob", "Dana"]
scores = [90, 85, 100]
pos = ['one', 'two', 'three']

for n, s in zip(names, scores):         #takes iterables, aggregates them in a tuple, and returns it
    print(n, s)
print(list(zip(names, scores, pos)))


x = 10
print(type(x))          # <class 'int'>
print(isinstance(x, float))  # True
a = "10"
b = int(a)
c = 3.5
d = int(c)
e = 123
f = float(e)
g = list("abc")
print(b, d, f, g)