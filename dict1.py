dict1 = {"key":"value"}

print(dict1.keys())
print(dict1.values())
print(dict1.items())

for k,v in dict1.items():
    print(k,v)

dict_gen = {k:k**2 for k in range(10)}

print(dict_gen)

print(dict_gen.popitem())

dict_gen.clear()

print(dict_gen)

dict_gen = dict1.copy()

print(dict_gen)

print(dict.fromkeys(["1","string"]))

print(dict.fromkeys([1,2],[3,4]))