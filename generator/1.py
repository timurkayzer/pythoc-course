# Generator

import random

# def gen():
#     yield 123
#     yield 123

# g = gen()

# print(next(g))
# print(next(g))
# print(next(g))


# for i in gen():
#     print(i)

def rand_gen(count):
    mem = []
    while True:
        n = random.randint(1,count)
        if n in mem:
            continue

        mem.append(n)
        yield n

        if len(mem) == count:
            return StopIteration
        
for el in rand_gen(10):
    print(el)