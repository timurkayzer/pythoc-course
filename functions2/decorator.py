def make_cool(fun):
    def wrap(*args):
        return "this is cool " + fun(*args)\

    return wrap

@make_cool
def hello(name):
    return "Hello {}".format(name)


print(hello("mike"))