c = lambda a,b : a*b

print(c(1,100))

def foo1(fn):
    fn()

foo1(lambda: print(1))

def clojure(n):
    return lambda a: a * n

mul50 = clojure(50)

print(mul50(2))