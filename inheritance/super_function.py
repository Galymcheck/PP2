class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)        #will make the child class inherit all the methods and properties from its parent:
    self.graduationyear = year             #we can add new property

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
