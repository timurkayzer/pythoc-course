# def foo(a,b):
#     print(a+b)

# foo(1,2)

def foo(*args):
    sum = 0
    for i in args:
        sum+=i
    print(sum)

foo(1,2,3,4,5)


def foo1(*args, **kwargs):
    sum = 0
    print(args)
    print(kwargs)
    for i in args:
        sum+=i
    print(sum)

foo1(1,2,3,4,5, action="multiply")