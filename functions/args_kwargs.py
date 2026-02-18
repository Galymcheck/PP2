def my_function(*args): #allows a function to accept any number of positional arguments.
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

def add_numbers(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(5, 10, 15, 20))


def my_function(**kwargs): #allows a function to accept any number of keyword arguments.
  print("Type:", type(kwargs))
  print("Name:", kwargs["name"])
  print("Age:", kwargs["age"])
  print("All data:", kwargs)

my_function(name = "Tobias", age = 30, city = "Bergen")