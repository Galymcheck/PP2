def my_function(name): #name is a parameter
  print("Hello", name)

my_function("Galamat") #"Galamat" is an argument


def fullname_function(firstname, lastname): #several arguments
  print(firstname + " " + lastname)

fullname_function("Galamat", "Tolepkazy")


def greet_user(name="Guest"): #If there is no argument, it uses the default value:
    print("Hello,", name)

greet_user()
greet_user("Galamat")


def pet_info(animal, name):
    print("I have a", animal)
    print("Its name is", name)

pet_info("cat", "Milo")

def pet_info(animal, name):
    print("I have a", animal)
    print("Its name is", name)

pet_info(name="Milo", animal="cat") #with keyword the order does not matter.