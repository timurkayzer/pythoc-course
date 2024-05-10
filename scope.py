g_var = 1

def foo():
    # global g_var
    g_var = 2

    def inner():
        # global g_var
        nonlocal g_var
        g_var+=1
    
    inner()
    print(g_var)

foo()

print(g_var)