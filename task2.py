# def sum_everything(a, b):
#     try:
#         return a + b
#     except:
#         type_a = type(a)
#         type_b = type(b)
#         if type_a == int and type_b == str:
#             return a + len(b)
#         elif type_a == str and type_b == int:
#             return "{}{}".format(a,b)
#         elif type_a == list:
#             a.add(b)
#         elif type_b == list:
#             return "{}{}".format(a,b)

# Пишите ваш код ниже этого комментария


# class MobilePhone:
#     _os:str 
#     _os_vendor:str
    
#     def info(self):
#         return "Mobile device based on {} by {}".format(self._os, self._os_vendor)
        
#     def call(self, phone_number:str):
#         if len(phone_number) == 11 and isnumeric(phone_number):
#             return "Calling to {} from {} phone".format(phone_number,self._os)
#         else:
#             return "Wrong phone number"


# class AndroidPhone(MobilePhone):
#     _os = "Android"
#     _os_vendor = "Google"

# class IPhone(MobilePhone):
#     _os = "iOS"
#     _os_vendor = "Apple"

# В этом задании нужно создать класс Temperature который может быть проинициализирован значениями celsius, fahrenheit или kelvin. После создания экземпляра у объекта должны быть доступны атрибуты которые позволяют получить представляения в остальных температурных представлениях. Никаких принтов не использовать, только возвращаемые значения.

# Пример работы:

# tmp_celsius_30 = Temperature(celsius=30)
# tmp_celsius_30.kelvin # -> 303.15
# tmp_celsius_30.fahrenheit # -> 86.00
# tmp_celsius_30.celsius # -> 30.00
# tmp_far_86 = Temperature(fahrenheit=86)
# tmp_far_86.kelvin # -> 303.15
# tmp_far_86.fahrenheit # -> 86.00
# tmp_far_86.celsius # -> 30.00
# Дополнительные требования:

# 1. Создать экземпляр без указания хотя бы одного из значений тоже нельзя, при попытке создать такой экземпляр Temperature() выбрасывать исключение ValueError.

# 2. Все значения температур округлять до двух знаков через round

class Temperature:
    kelvin = None
    fahrenheit = None
    celsius = None

    def __init__(self, kelvin=None, fahrenheit=None, celsius=None) -> None:
        if kelvin != None:
            self.kelvin = kelvin
            self.celsius = kelvin - 273.15
            self.fahrenheit = kelvin*1.8-459.67
        elif fahrenheit != None:
            self.fahrenheit = fahrenheit
            self.kelvin = (fahrenheit + 459,67)/1.8
            self.celsius = (fahrenheit + 32)/1.8
        elif celsius != None:
            self.celsius = celsius
            self.kelvin = celsius + 273.15
            self.fahrenheit = celsius*1.8+32
        else:
            raise ValueError()
        
        self.kelvin = round(self.kelvin,2)
        self.celsius = round(self.celsius,2)
        self.fahrenheit = round(self.fahrenheit,2)
