def my_function():
  print("Hello World")
def get_greeting():
  return "Hello from a function"


my_function()

message = get_greeting()
print(message)


def print_numbers(numbers): #passing list
    for num in numbers:
        print(num)

print_numbers([1, 2, 3, 4, 5])

def print_student(student): #passing dictionary
    print("Name:", student["name"])
    print("Age:", student["age"])

student_info = {
    "name": "Galam",
    "age": 18
}

print_student(student_info)


def multiply(a, b): #docstring
    """
    This function multiplies two numbers.

    Parameters:
    a (int): first number
    b (int): second number

    Returns:
    int: result of multiplication
    """
    return a * b

print(multiply(3, 4))