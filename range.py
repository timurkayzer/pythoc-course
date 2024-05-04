print(range(16))

for el in range(5,20,3):
    print(el)

    
for el in range(20,5,-1):
    print(el)

some_list = list(range(20))
t = [el**2 for el in some_list if not el % 2]
print(t)

some_list = list(range(20))
t = [some_list[i]**2 for i in range(len(some_list)) if not i % 2]
print(t)