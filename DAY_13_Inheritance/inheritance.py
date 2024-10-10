#base class (parent class/super class)
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name} makes a sound"
    
# Dreived class (subclass) inheriting from animal    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says barks!"

# Dreived class (subclass) inheriting from animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# Creating objects of derived classes
dog =Dog("Jonny")
cat= Cat("Manzar")

print(dog.speak())
print(cat.speak())
    
    
