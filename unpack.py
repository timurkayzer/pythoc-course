l = [1,2,3,4]

print(l)
print(*l)

d1 = {"a":1,"b":2}
d2 = {**d1, "b":3}
d3 = {"b":1,**d1}

print(d3)
print(d2)

a,b,c,*d,e,f = 1,2,3,4,5,6,7,8,9,0

print(a,b,c,d,e,f)