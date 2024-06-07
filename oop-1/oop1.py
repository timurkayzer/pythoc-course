class Car:
    wheels = 4

    def move(self):
        print("began to move with {} wheels".format(self.wheels))

    def setWheels(self, wheels:int):
        self.wheels = wheels

toyota = Car()
honda = Car()

toyota.setWheels(6)

toyota.move()
honda.move()
