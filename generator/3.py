def my_generator(value: int, power: int, amount: int):
    i = value
    while i < value + amount:
        yield i**power
        i+=1
    return StopIteration

for i in my_generator(12,2,5):
    print(i)