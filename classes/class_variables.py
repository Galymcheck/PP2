class Person:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age        # instance variable

p1 = Person("Emil", 36)
p2 = Person("Anna", 25)

print(p1.name, p1.age)  # Emil
print(p2.name, p2.age)  # Anna

class Person2:
    species = "Human"   # class variable, belongs to all objects

    def __init__(self, name):
        self.name = name

p1 = Person2("Emil")
p2 = Person2("Anna")

print(p1.name, p1.species)
print(p2.name, p2.species)

