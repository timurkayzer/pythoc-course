l1 = [1,2,3,4,5]
l2 = ["",False, None, 0, []]

print(any(l1))
print(any(l2))

print(all(l1))
print(all(l2))

print(list(zip(l1,l2,range(3))))