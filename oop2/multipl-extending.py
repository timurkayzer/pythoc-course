class Animal:
    def sound(self):
        pass
    
class Swimming:
    def swim(self):
        pass

class Running:
    def run(self):
        pass

class Fish(Animal, Swimming):
    pass

fish = Fish()

fish.sound()

fish.swim()