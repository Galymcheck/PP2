class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def call(self):   #name of method must be different
        print("Calling...")

class Smartphone(Camera, Phone):
    pass

s = Smartphone()
s.take_photo()
s.call()
