class Car:
    def drive(self):
        print("drive")

class Toyota(Car):
    def drive(self):
        print("drive fast")

prado = Toyota()
prado.drive()