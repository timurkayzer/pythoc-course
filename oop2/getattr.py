# getattr setattr hasattr

class Example:
    def foo():
        pass
    pass

e = Example()

print(e)

setattr(e, "testatt", "111")
print(getattr(e,"testatt"))
print(hasattr(e,"testatt"))
print(hasattr(e,"foo"))

