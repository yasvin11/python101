class Animal: 
    def __init__(self, name, color, sex):
        self.name = name
        self.color = color
        self.sex = sex

class Cat(Animal):
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")
        
class Horse(Animal):
    def neigh(self):
        print("Neighhh!")

fido = Dog("Fido", "brown","F")
print(fido.name)
print(fido.color)
print(fido.sex)
fido.bark()

tom = Cat("Tom", "ginger", "M")
print(tom.name)
print(tom.color)
print(tom.sex)
tom.purr()

selby = Horse("Selby", "black", "M")
print(selby.name)
print(selby.color)
print(selby.sex)
selby.neigh()
