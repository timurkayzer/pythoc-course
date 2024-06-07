dict1 = dict(key="value")
dict2 = {"key":"value"}
dict3 = dict([("key1","value1")])

print(dict1.get("key1"))
print(dict2)
print(dict3)


dict4 = {(100,500):500}

print(dict4)

dict4[(100,500)] = 400

print(dict4)