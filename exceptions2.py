class NegativeNumberException(Exception):
    def __init__(self, message) -> None:
        self.message = message
    pass



argument1 = input("arg 1: ")
argument2 = input("arg 2: ")
action = input("action: ")

statement = "print({} {} {})".format(argument1,action, argument2)

try:
    if int(argument1) < 0 or int(argument2) < 0:
        raise NegativeNumberException("No negative numbers")
    eval(statement)
except NegativeNumberException as e:
    print("Only positive numbers")
except Exception as e:
    print(e)
    print("Unexpected exception")
else:
    print("All OK")
finally:
    print("Code executed")