class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):   #same name of method from parent class, but different result
        print("The dog barks")

a = Animal()
d = Dog()

a.speak()  # The animal makes a sound
d.speak()  # The dog barks
