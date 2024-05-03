height = int(input("Введите высоту: "))

i = 1
length = height*2 - 1
while i <= height:
    str = ""
    j = 0
    while j<length:
        if i > abs(length - height - j):
            str += "*"
        else:
            str += " "
        j+=1
    i+=1
    