class ExampleCar:
    __wheels:str

    def __init__(self, wheels=4) -> None:
        self.__wheels = wheels
        pass

    @classmethod
    def setGlobalWheels(c,wheels):
        c.__wheels = wheels

car = ExampleCar(6)

print(car.wheels)
print(getattr(car,"wheels"))
print(type(getattr(car,"wheels")))
print(hasattr(car,"wheels"))
car.wheels = 4
print(car.wheels)

print(ExampleCar.getName("toyota"))