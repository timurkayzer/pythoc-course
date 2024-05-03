target = [1,2,3,4,5,6]
str = "this is string"

i = 0
while i < len(target):
    print(target[i])
    if i == 3:
        break
    i+=1
    continue

i = 0
for c in range(len(str)):
    print(str[c])

for c in str:
    print(c)
else:
    print('loop ended')