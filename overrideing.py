class Animal:
    def speak(self):
        print("Animal not speak")

class Dog(Animal):
    def speak(self):
        print("Dog not speak")   

class Cat(Animal):
    def speak(self):
        print("cat not speak")

obj=Dog()
obj.speak()        