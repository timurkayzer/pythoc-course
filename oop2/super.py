class Rectangle:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

class Square(Rectangle):
    def __init__(self,a) -> None:
        super().__init__(a,a)

s = Square(5)
print(s.a)
print(s.b)
