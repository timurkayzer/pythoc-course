l = [1,3,4,5]
l2 = l.copy()

l1 = map(lambda el1,el2: el1*el2, l, l2)

print(list(l1))