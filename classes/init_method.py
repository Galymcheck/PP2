class Person:  #used to create objects with initial values:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

"""
p1                       p2
 ├── name = "Emil"        ├── name = "Tobias"  
 └── age = 18             └── age = 25
 """