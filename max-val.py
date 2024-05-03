# Так как это задание связано с выводом на экран, то нормально его проверить тестами нет возможности в рамках платформы Udemy.
# С одним из вариантов решения можно свериться тут: https://gist.github.com/konflic/ea02f5688e56d1f11a23bf6feb9c267c

lst = [100, 12, 2, 33, 4, 10, 100, 21, 90, 99, 100, -10]
max_i = []
max_i.append(0)
for i in range(len(lst)):
    if i == 0:
        continue
    if lst[i] > lst[max_i[0]]:
        max_i.clear()
        max_i.append(i)
    elif lst[i] == lst[max_i[0]]:
        max_i.append(i)
        
print(max_i)
