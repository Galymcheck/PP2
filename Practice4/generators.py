# 1. Generator that generates squares up to N
def squares_numbers(n):        #A generator function is a special type of function 
    for i in range(n):         #that returns an iterator object.
        yield i*i            #use yield to produce a series of results over time.
                               

# 2. Print even numbers between 0 and n (comma separated)
def even_numbers(n):
    for i in range(n):
        if i%2 == 0:
            yield i


# 3. Generator for numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n):
        if i%3 == 0 and i%4 == 0:
            yield i


# 4. Generator squares from a to b
def squares(a, b):
    for i in range(a, b):
        yield i*i


# 5. Generator that returns numbers from n down to 0
def countdown(n):
    while n>=0:
        yield n
        n-=1



n = int(input("Enter n: "))

print("\n#1 Squares up to n:")
for x in squares_numbers(n):
    print(x, end=" ")


print("\n#2 Even numbers:")
for x in even_numbers(n):
    print(x, end=" ")


print("\n#3 Numbers divisible by 3 and 4:")
for x in divisible_by_3_and_4(n):
    print(x, end=" ")


print("\n#4 Squares from a to b:")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for x in squares(a, b):
    print(x, end=" ")


print("\n#5 Countdown from n to 0:")
for x in countdown(n):
    print(x, end=" ")