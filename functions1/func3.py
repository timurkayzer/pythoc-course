def foo(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(1)
    print(my_list)

foo()
foo()
foo()
foo()
