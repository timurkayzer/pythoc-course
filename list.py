# list1 = list("abc")
# str = "string"
# list2 = ['a',True, False]

# print(list1)

# list1.reverse()

# print(list1[-1])

# print(list1 + list2)

# print(False)

# list1.append("12121")

# print(list1)

# print(list1[-2:-1])

# list3 = list1

# list3.append("test")

# print(list1 == list3)

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
list3 = ["a",None,True,[]]

print(id(list1) == id(list2))
print(list1 >= list2)

print(list1.count(1))

# inserts into position
list1.insert(0,7)

print(list1)

print(1 in list1)

list2.extend([9,10,11])

print(list2)

list2.pop(-1)

list2.remove(9)

print(list2)

list1.sort(reverse=True)

print(list1)

list1.insert(100, 55)

print(list1)