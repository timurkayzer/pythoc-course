# Iterator
import random


l = [1,2,3]

i = iter(l)

print(next(i))

class RndNums:

    def __init__(self,amount):
        self.amount = amount
        self.mem = []

    def __iter__(self):
        return self

    def __next__(self):
        n = random.randint(1,self.amount)
        if len(self.mem) == self.amount:
            raise StopIteration
        self.mem.append(n)
        return n
    
rn = RndNums(20)

for el in rn:
    print(el)
