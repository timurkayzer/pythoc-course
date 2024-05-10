from random import randint

print("Угадай число!")
try:
    max = int(input("Введите верхний лимит: "))
except:
    print("Введено некорректное число, автоматически выбран лимит 100")
    max = 100
rand = randint(0,max)
guess = None
tries = 0
while guess != rand:
    if guess != None:
        if guess > rand:
            print("Перебор")
        else:
            print("Недобор")
    try:
        guess = int(input("Введите число: "))
    except:
        print("Введите корректное число!")
        guess = None
        continue
    tries+=1

print(f"Верно! Заняло {tries} попыток")