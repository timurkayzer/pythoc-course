class Vehicle:
    def __init__(self, name, wheels) -> None:
        self.wheels = wheels
        self.name = name

    def move(self):
        print("start moving {} on {} wheels".format(self.name, self.wheels))

    def set_wheels(self,wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass
    

toyota = Car("toyota",4)

toyota.move()

print(issubclass(Car,Vehicle))

print(isinstance(toyota,Vehicle))