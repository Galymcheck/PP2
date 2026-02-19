class Person:   #parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):   #child class
  pass

x = Student("Mike", "Olsen")
x.printname()
