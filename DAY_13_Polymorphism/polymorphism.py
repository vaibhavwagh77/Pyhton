#base class (parent class/super class)
class Animal:
    def __init__(self,name):
        print("In constructor of Animal.")
        self.name=name
    def speak(self):
        print("Animal have sound.")
        return f"{self.name} makes a sound"
    
# Dreived class (subclass) inheriting from animal    
class Dog(Animal):
    def __init__(self,name):
        print("In constructor of Dog.")
        self.name=name
    def speak(self):
        return f"{self.name} says barks!"

# Dreived class (subclass) inheriting from animal
class Cat(Animal):
    def __init__(self,name):
        print("In constructor of Cat.")
        self.name=name
    def speak(self):
        return f"{self.name} says meow!"

# Creating objects of derived classes
dog =Dog("Jonny")
cat= Cat("Manzar")

print(dog.speak())
print(cat.speak())
    
    