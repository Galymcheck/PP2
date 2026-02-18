def get_greeting():
  return "Hello from a function" #send data back to the code that called them

message = get_greeting()
print(message)


def square(x):
    return x * x

result = square(5)
print(result)


def my_function():
  return ["apple", "banana", "cherry"] #A function that returns a list:

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])