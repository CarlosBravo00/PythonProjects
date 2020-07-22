
class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getage(self):
        print("Age:",self.age)

class dog(animal):
    def talk(self):
        print(self.name,"says: woof")

class cat(animal):
    def talk(self):
        print(self.name,"says: meow")

cuco = dog("Don Pedro",10)
cuco.talk()
h = cat('Miercoles',8)
h.talk()
cuco.getage()
h.getage()
