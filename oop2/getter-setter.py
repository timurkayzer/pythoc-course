class ExampleCar:
    __wheels:str

    def __init__(self, wheels=4) -> None:
        self.__wheels = wheels
        pass

    @property
    def wheels(self):
        return self.__wheels
    
    @wheels.setter
    def wheels(self,wheels):
        self.__wheels = wheels
    
    @wheels.deleter
    def wheels(self):
        self.__wheels = 0

    @staticmethod
    def getName(name):
        return "name is "+name

car = ExampleCar(6)

print(car.wheels)
print(getattr(car,"wheels"))
print(type(getattr(car,"wheels")))
print(hasattr(car,"wheels"))
car.wheels = 4
print(car.wheels)

print(ExampleCar.getName("toyota"))