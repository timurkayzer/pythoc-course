argument1 = input("arg 1: ")
argument2 = input("arg 2: ")
action = input("action: ")

statement = "print({} {} {})".format(argument1,action, argument2)

try:
    eval(statement)
# except ZeroDivisionError:
#     print("Cannot divide by 0")
# except NameError:
#     print("Input numbers as arguments")
# except TypeError:
#     print("Arguments must have valid types")
except Exception as e:
    print(dir(e))
    print("Unexpected exception")
else:
    print("All OK")
finally:
    print("Code executed")